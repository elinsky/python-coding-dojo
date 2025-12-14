#!/usr/bin/env python3
"""Generate burndown chart for EPI problem progress tracking.

Two burndowns:
1. Exposure: Total attempts remaining to reach 2 per problem (capped at 2) -> target 0 by Dec 24
2. Mastery: 90% of P0-P2 at mastery tier -> target by Dec 31
"""

from datetime import date, datetime, timedelta
from pathlib import Path
import yaml
import matplotlib.pyplot as plt
import matplotlib.dates as mdates


# Configuration
START_DATE = date(2025, 12, 13)
EXPOSURE_TARGET_DATE = date(2025, 12, 24)
MASTERY_TARGET_DATE = date(2025, 12, 31)
MASTERY_TARGET_PERCENT = 90
MASTERY_TIME_THRESHOLD = 20  # minutes


def analyze_problem_for_burndown(problem_data, threshold=MASTERY_TIME_THRESHOLD, as_of_date=None):
    """Analyze a problem for burndown metrics.

    If as_of_date is provided, only count attempts with date <= as_of_date.
    """
    attempts = problem_data.get('attempts', [])

    # Filter attempts by date if as_of_date is provided
    if as_of_date is not None:
        filtered_attempts = []
        for attempt in attempts:
            attempt_date_str = attempt.get('date', '')
            if attempt_date_str:
                # Parse ISO format date string
                attempt_dt = datetime.fromisoformat(attempt_date_str)
                attempt_date = attempt_dt.date()
                if attempt_date <= as_of_date:
                    filtered_attempts.append(attempt)
        attempts = filtered_attempts

    attempt_count = len(attempts)

    is_mastered = False
    for attempt in attempts:
        if not attempt.get('solved', False):
            continue
        if attempt.get('used_hints', False) or attempt.get('used_solution', False):
            continue
        time_minutes = attempt.get('time_minutes')
        if time_minutes is not None and time_minutes <= threshold and attempt.get('optimal', False):
            is_mastered = True
            break

    return {
        'attempts': attempt_count,
        'is_mastered': is_mastered,
    }


def calculate_burndown_stats(problems, as_of_date=None):
    """Calculate burndown statistics for P0-P2 problems.

    If as_of_date is provided, only count attempts with date <= as_of_date.
    """
    stats = {
        'total_problems': 0,
        'needs_exposure': 0,  # Total attempts remaining to reach 2 per problem
        'mastered': 0,
        'problems_detail': [],
    }

    for problem_id, problem_data in problems.items():
        problem_num = problem_data.get('problem_number', '')
        if problem_num.endswith('.00'):
            continue

        priority = problem_data.get('priority', '')
        if priority not in ['P0', 'P1', 'P2']:
            continue

        stats['total_problems'] += 1
        analysis = analyze_problem_for_burndown(problem_data, as_of_date=as_of_date)

        # Count attempts remaining to reach 2 (capped at 2 per problem)
        # 0 attempts -> +2, 1 attempt -> +1, 2+ attempts -> +0
        attempts_remaining = max(0, 2 - analysis['attempts'])
        stats['needs_exposure'] += attempts_remaining

        if analysis['is_mastered']:
            stats['mastered'] += 1

        stats['problems_detail'].append({
            'id': problem_id,
            'name': problem_data.get('name', problem_id),
            'priority': priority,
            'problem_number': problem_num,
            'attempts': analysis['attempts'],
            'is_mastered': analysis['is_mastered'],
        })

    stats['mastery_target'] = int(stats['total_problems'] * MASTERY_TARGET_PERCENT / 100)
    stats['needs_mastery'] = max(0, stats['mastery_target'] - stats['mastered'])

    # Starting values (as of START_DATE)
    # Exposure: attempts remaining to reach 2 per problem
    # On Dec 13 (commit b86a6fa): 22 had 0 attempts, 17 had 1 attempt, 20 had 2+
    # So: (22*2) + (17*1) + (20*0) = 44 + 17 + 0 = 61 attempts remaining
    stats['start_exposure'] = 61  # Fixed: attempts remaining on Dec 13
    stats['start_mastery'] = 30   # Fixed: what we needed on Dec 13

    return stats


def calculate_historical_stats(problems, start_date, end_date):
    """Calculate burndown stats for each day from start_date to end_date.

    Returns list of (date, exposure_remaining, mastery_remaining) tuples.
    """
    history = []
    current_date = start_date
    while current_date <= end_date:
        stats = calculate_burndown_stats(problems, as_of_date=current_date)
        history.append((current_date, stats['needs_exposure'], stats['needs_mastery']))
        current_date += timedelta(days=1)
    return history


def calculate_ahead_behind(current_remaining, start_remaining, start_date, target_date):
    """Calculate how many problems ahead/behind schedule.

    Assumes you need to complete today's work - so at start of any day,
    you're "behind" until you do that day's problems.
    """
    today = date.today()

    if today >= target_date:
        # Past target date
        return -current_remaining if current_remaining > 0 else 0

    total_days = (target_date - start_date).days
    days_elapsed = (today - start_date).days

    if total_days <= 0:
        return 0

    # Expected remaining by END of today (include today's work as expected)
    # days_elapsed + 1 because we expect today's work to be done
    daily_rate = start_remaining / total_days
    expected_remaining = start_remaining - (daily_rate * (days_elapsed + 1))

    # Positive = ahead, negative = behind
    return expected_remaining - current_remaining


def generate_staircase_target(start_remaining, start_date, target_date):
    """Generate staircase target line coordinates.

    Pattern: At start of each day, drop vertically to target, then horizontal until next day.
    Visual: On Dec 13, starts at 38, immediately drops to 35, stays at 35 until Dec 14.

    Returns lists of dates and values for plotting with ax.plot().
    """
    total_days = (target_date - start_date).days
    daily_rate = start_remaining / total_days

    dates = []
    values = []

    # Very first point - before any work
    dates.append(start_date)
    values.append(start_remaining)

    for day_offset in range(total_days):
        current_date = start_date + timedelta(days=day_offset)
        next_date = current_date + timedelta(days=1)

        # Target after this day's work
        target_value = start_remaining - (daily_rate * (day_offset + 1))
        target_value = max(0, target_value)

        # Drop down to target (same x, lower y)
        dates.append(current_date)
        values.append(target_value)

        # Horizontal line to next day (different x, same y)
        dates.append(next_date)
        values.append(target_value)

    return dates, values


def generate_burndown_chart(stats, output_path, problems=None):
    """Generate matplotlib burndown chart with staircase style."""
    today = date.today()

    # Get historical data if problems provided
    history = []
    if problems is not None:
        history = calculate_historical_stats(problems, START_DATE, today)

    # Create figure with two subplots
    fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))
    fig.suptitle('Burndown Progress', fontsize=14, fontweight='bold')

    # --- Exposure Burndown ---
    exp_start = stats['start_exposure']
    exp_current = stats['needs_exposure']
    exp_target_date = EXPOSURE_TARGET_DATE

    # Target staircase (full timeline)
    exp_target_dates, exp_target_values = generate_staircase_target(
        exp_start, START_DATE, exp_target_date
    )

    days_elapsed = (today - START_DATE).days
    daily_rate = exp_start / (exp_target_date - START_DATE).days

    ax1.plot(exp_target_dates, exp_target_values, 'b--', linewidth=2, label='Target', alpha=0.7)

    # Plot actual line with dots for each day
    if history:
        hist_dates = [h[0] for h in history]
        hist_exposure = [h[1] for h in history]
        # Line connecting dots
        ax1.plot(hist_dates, hist_exposure, 'g-', linewidth=2, alpha=0.7)
        # Dots for each day
        ax1.scatter(hist_dates, hist_exposure, color='green', s=100, zorder=5,
                    edgecolors='darkgreen', linewidths=2, label='Actual')
    else:
        # Fallback: just show today's dot
        ax1.scatter([today], [exp_current], color='green', s=150, zorder=5,
                    edgecolors='darkgreen', linewidths=2, label='Actual')

    # Ahead/behind calculation
    exp_ahead = calculate_ahead_behind(exp_current, exp_start, START_DATE, exp_target_date)
    exp_status = f"+{exp_ahead:.1f} ahead" if exp_ahead >= 0 else f"{exp_ahead:.1f} behind"

    ax1.set_title(f'Exposure (attempts to 2 each)\n{exp_status}', fontsize=12)
    ax1.set_xlabel('Date')
    ax1.set_ylabel('Problems Remaining')
    ax1.set_ylim(bottom=0, top=exp_start + 5)
    ax1.set_xlim(START_DATE - timedelta(days=1), exp_target_date + timedelta(days=0.5))
    ax1.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax1.xaxis.set_major_locator(mdates.DayLocator(interval=2))
    ax1.legend(loc='upper right')
    ax1.grid(True, alpha=0.3)
    ax1.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    # Annotate current value
    ax1.annotate(f'{exp_current}', (today, exp_current), textcoords="offset points",
                 xytext=(10, 5), fontsize=10, fontweight='bold', color='green')

    # --- Mastery Burndown ---
    mast_start = stats['start_mastery']
    mast_current = stats['needs_mastery']
    mast_target_date = MASTERY_TARGET_DATE

    # Target staircase
    mast_target_dates, mast_target_values = generate_staircase_target(
        mast_start, START_DATE, mast_target_date
    )

    ax2.plot(mast_target_dates, mast_target_values, 'b--', linewidth=2, label='Target', alpha=0.7)

    # Plot actual line with dots for each day
    if history:
        hist_dates = [h[0] for h in history]
        hist_mastery = [h[2] for h in history]
        # Line connecting dots
        ax2.plot(hist_dates, hist_mastery, 'g-', linewidth=2, alpha=0.7)
        # Dots for each day
        ax2.scatter(hist_dates, hist_mastery, color='green', s=100, zorder=5,
                    edgecolors='darkgreen', linewidths=2, label='Actual')
    else:
        # Fallback: just show today's dot
        ax2.scatter([today], [mast_current], color='green', s=150, zorder=5,
                    edgecolors='darkgreen', linewidths=2, label='Actual')

    # Ahead/behind calculation
    mast_ahead = calculate_ahead_behind(mast_current, mast_start, START_DATE, mast_target_date)
    mast_status = f"+{mast_ahead:.1f} ahead" if mast_ahead >= 0 else f"{mast_ahead:.1f} behind"

    ax2.set_title(f'Mastery (90% at mastery tier)\n{mast_status}', fontsize=12)
    ax2.set_xlabel('Date')
    ax2.set_ylabel('Problems Remaining')
    ax2.set_ylim(bottom=0, top=mast_start + 5)
    ax2.set_xlim(START_DATE - timedelta(days=1), mast_target_date + timedelta(days=0.5))
    ax2.xaxis.set_major_formatter(mdates.DateFormatter('%b %d'))
    ax2.xaxis.set_major_locator(mdates.DayLocator(interval=3))
    ax2.legend(loc='upper right')
    ax2.grid(True, alpha=0.3)
    ax2.axhline(y=0, color='black', linestyle='-', linewidth=0.5)

    # Annotate current value
    ax2.annotate(f'{mast_current}', (today, mast_current), textcoords="offset points",
                 xytext=(10, 5), fontsize=10, fontweight='bold', color='green')

    plt.tight_layout()
    plt.savefig(output_path, dpi=150, bbox_inches='tight', facecolor='white')
    plt.close()

    return {
        'exposure_ahead': exp_ahead,
        'mastery_ahead': mast_ahead,
    }


def generate_burndown_section(stats, chart_path='images/burndown.png'):
    """Generate markdown section for burndown display."""
    today = date.today()

    exposure_days = (EXPOSURE_TARGET_DATE - today).days
    mastery_days = (MASTERY_TARGET_DATE - today).days

    exp_ahead = calculate_ahead_behind(
        stats['needs_exposure'], stats['start_exposure'], START_DATE, EXPOSURE_TARGET_DATE
    )
    mast_ahead = calculate_ahead_behind(
        stats['needs_mastery'], stats['start_mastery'], START_DATE, MASTERY_TARGET_DATE
    )

    exp_status = f"**+{exp_ahead:.1f} ahead**" if exp_ahead >= 0 else f"**{exp_ahead:.1f} behind**"
    mast_status = f"**+{mast_ahead:.1f} ahead**" if mast_ahead >= 0 else f"**{mast_ahead:.1f} behind**"

    # Daily rates needed from today
    exp_rate = stats['needs_exposure'] / exposure_days if exposure_days > 0 else stats['needs_exposure']
    mast_rate = stats['needs_mastery'] / mastery_days if mastery_days > 0 else stats['needs_mastery']

    lines = [
        '## Burndown Progress',
        '',
        f'![Burndown Chart]({chart_path})',
        '',
        f'| Metric | Exposure | Mastery |',
        f'|--------|----------|---------|',
        f'| Remaining | {stats["needs_exposure"]} | {stats["needs_mastery"]} |',
        f'| Target Date | Dec 24 ({exposure_days}d) | Dec 31 ({mastery_days}d) |',
        f'| Rate Needed | {exp_rate:.1f}/day | {mast_rate:.1f}/day |',
        f'| Status | {exp_status} | {mast_status} |',
        '',
    ]

    return lines


def get_burndown_stats(progress_file=None):
    """Load progress data and return burndown stats."""
    if progress_file is None:
        repo_root = Path(__file__).parent.parent
        progress_file = repo_root / 'progress.yaml'

    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    problems = data.get('problems', {})
    return calculate_burndown_stats(problems)


def generate_chart(progress_file=None, output_path=None):
    """Generate the burndown chart image."""
    if progress_file is None:
        repo_root = Path(__file__).parent.parent
        progress_file = repo_root / 'progress.yaml'

    if output_path is None:
        repo_root = Path(__file__).parent.parent
        output_path = repo_root / 'images' / 'burndown.png'

    # Ensure images directory exists
    output_path.parent.mkdir(parents=True, exist_ok=True)

    # Load problems for historical data
    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)
    problems = data.get('problems', {})

    stats = get_burndown_stats(progress_file)
    return generate_burndown_chart(stats, output_path, problems=problems)


def main():
    """Generate burndown chart and print status."""
    repo_root = Path(__file__).parent.parent
    progress_file = repo_root / 'progress.yaml'
    output_path = repo_root / 'images' / 'burndown.png'

    # Load problems for historical data
    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)
    problems = data.get('problems', {})

    stats = get_burndown_stats(progress_file)

    # Generate chart
    output_path.parent.mkdir(parents=True, exist_ok=True)
    status = generate_burndown_chart(stats, output_path, problems=problems)

    print(f"Generated: {output_path}")
    print(f"\nExposure: {stats['needs_exposure']} remaining", end="")
    if status['exposure_ahead'] >= 0:
        print(f" (+{status['exposure_ahead']:.1f} ahead)")
    else:
        print(f" ({status['exposure_ahead']:.1f} behind)")

    print(f"Mastery: {stats['needs_mastery']} remaining", end="")
    if status['mastery_ahead'] >= 0:
        print(f" (+{status['mastery_ahead']:.1f} ahead)")
    else:
        print(f" ({status['mastery_ahead']:.1f} behind)")


if __name__ == '__main__':
    main()
