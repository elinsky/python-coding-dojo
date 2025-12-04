#!/usr/bin/env python3
"""Generate README.md from progress.yaml with emoji-based progress visualization."""

from datetime import datetime
from pathlib import Path
from collections import defaultdict
import yaml
import click


def analyze_problem(problem_data, threshold):
    """Analyze a problem's attempts and return its tier and best time.

    Returns:
        tuple: (tier, best_time, has_attempts)
            tier: 0 (attempted/unsolved), 1 (solved), 2 (independent), 3 (mastered)
            best_time: minimum time in minutes for tier 2+ attempts, None otherwise
            has_attempts: True if problem has any attempts, False otherwise
    """
    attempts = problem_data.get('attempts', [])

    # Never attempted
    if not attempts:
        return 0, None, False

    # Track best independent time
    best_time = None
    tier = 0

    for attempt in attempts:
        if not attempt.get('solved', False):
            continue

        # At least tier 1 (solved)
        if tier < 1:
            tier = 1

        # Check if independent (no hints, no solution)
        if not attempt.get('used_hints', False) and not attempt.get('used_solution', False):
            if tier < 2:
                tier = 2

            # Track best time for independent attempts
            time_minutes = attempt.get('time_minutes')
            if time_minutes is not None:
                if best_time is None or time_minutes < best_time:
                    best_time = time_minutes

                # Check if mastered (independent + fast + optimal)
                if time_minutes <= threshold and attempt.get('optimal', False):
                    tier = 3

    return tier, best_time, True


def format_time(seconds):
    """Format seconds as m:ss or mm:ss."""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


def generate_flashcard_section(flashcards):
    """Generate the flashcard drills section for README.

    Only includes categories that have a target_seconds defined.

    Args:
        flashcards: Dict of flashcard categories from progress.yaml

    Returns:
        list: Lines for the flashcard section, or empty list if no categories with targets
    """
    if not flashcards:
        return []

    # Filter to only categories with targets
    categories_with_targets = {
        key: data for key, data in flashcards.items()
        if data.get('target_seconds') is not None
    }

    if not categories_with_targets:
        return []

    lines = [
        '## Python Flashcards',
        '',
        '| Category | Status | Target Score | Actual Score | Target Time | Actual Time | Last Drilled |',
        '|----------|--------|--------------|--------------|-------------|-------------|--------------|',
    ]

    for category_id, category_data in categories_with_targets.items():
        name = category_data.get('name', category_id)
        target_seconds = category_data['target_seconds']
        attempts = category_data.get('attempts', [])

        # Get most recent attempt
        if attempts:
            latest = attempts[0]  # Assumes attempts are in reverse chronological order
            count = latest.get('count', 0)
            score = latest.get('score', 0)
            time_seconds = latest.get('time_seconds', 0)

            # Determine pass/fail: perfect score AND under time
            passed = (score == count) and (time_seconds <= target_seconds)
            status = '✅' if passed else '⬜'

            target_score = f"{count}/{count}"
            actual_score = f"{score}/{count}"
            actual_time = format_time(time_seconds)

            # Extract date from ISO format (YYYY-MM-DDTHH:MM:SS)
            date_str = latest.get('date', '')
            if date_str:
                last_drilled = date_str.split('T')[0]  # Get just YYYY-MM-DD
            else:
                last_drilled = '—'
        else:
            status = '⬜'
            target_score = '—'
            actual_score = '—'
            actual_time = '—'
            last_drilled = '—'

        target_time = format_time(target_seconds)
        lines.append(f'| {name} | {status} | {target_score} | {actual_score} | {target_time} | {actual_time} | {last_drilled} |')

    lines.append('')
    return lines


def generate_progress_bar(count, total, emoji):
    """Generate emoji-based progress bar with 20 emojis per line.

    Args:
        count: Number of completed items
        total: Total number of items
        emoji: Emoji to use for completed items (e.g., '👍', '💪', '🏆')

    Returns:
        str: Multi-line progress bar string
    """
    emojis_per_line = 20
    lines = []
    current_line = ''

    # Fill with completed emoji, then empty squares
    for i in range(total):
        if i < count:
            current_line += emoji
        else:
            current_line += '⬜'

        # Start new line after 20 emojis
        if (i + 1) % emojis_per_line == 0:
            lines.append(current_line)
            current_line = ''

    # Add any remaining emojis
    if current_line:
        lines.append(current_line)

    return '\n'.join(lines)


def calculate_stats(problems, threshold):
    """Calculate overall and per-chapter statistics.

    Returns:
        dict: {
            'tier0': int,
            'tier1': int,
            'tier2': int,
            'tier3': int,
            'total': int,
            'chapters': {
                chapter_name: {
                    'tier0': int,
                    'tier1': int,
                    'tier2': int,
                    'tier3': int,
                    'total': int,
                    'chapter_num': str
                }
            },
            'problems_by_tier': {
                problem_id: {
                    'tier': int,
                    'best_time': int or None,
                    'has_attempts': bool,
                    'metadata': dict
                }
            },
            'priority_stats': {
                'P0': {'total': int, 'attempted': int, 'mastered': int},
                ...
            }
        }
    """
    stats = {
        'tier0': 0,
        'tier1': 0,
        'tier2': 0,
        'tier3': 0,
        'total': 0,
        'chapters': defaultdict(lambda: {'tier0': 0, 'tier1': 0, 'tier2': 0, 'tier3': 0, 'total': 0, 'chapter_num': ''}),
        'problems_by_tier': {},
        'priority_stats': {
            'P0': {'total': 0, 'attempted': 0, 'mastered': 0},
            'P1': {'total': 0, 'attempted': 0, 'mastered': 0},
            'P2': {'total': 0, 'attempted': 0, 'mastered': 0},
            'P3': {'total': 0, 'attempted': 0, 'mastered': 0},
            'P4': {'total': 0, 'attempted': 0, 'mastered': 0},
        }
    }

    for problem_id, problem_data in problems.items():
        # Skip bootcamp problems (problem numbers ending in .00)
        problem_num = problem_data.get('problem_number', '')
        if problem_num.endswith('.00'):
            continue

        stats['total'] += 1
        tier, best_time, has_attempts = analyze_problem(problem_data, threshold)

        # Store problem analysis
        stats['problems_by_tier'][problem_id] = {
            'tier': tier,
            'best_time': best_time,
            'has_attempts': has_attempts,
            'metadata': problem_data
        }

        # Update overall stats
        if tier >= 0 and has_attempts:
            stats['tier0'] += 1
        if tier >= 1:
            stats['tier1'] += 1
        if tier >= 2:
            stats['tier2'] += 1
        if tier >= 3:
            stats['tier3'] += 1

        # Update chapter stats
        chapter_name = problem_data.get('chapter_name', 'Unknown')
        chapter_num = problem_data.get('problem_number', '').split('.')[0]

        chapter_stats = stats['chapters'][chapter_name]
        chapter_stats['total'] += 1
        chapter_stats['chapter_num'] = chapter_num

        if tier >= 0 and has_attempts:
            chapter_stats['tier0'] += 1
        if tier >= 1:
            chapter_stats['tier1'] += 1
        if tier >= 2:
            chapter_stats['tier2'] += 1
        if tier >= 3:
            chapter_stats['tier3'] += 1

        # Update priority-based stats for goals
        priority = problem_data.get('priority', '')
        if priority in stats['priority_stats']:
            priority_stat = stats['priority_stats'][priority]
            priority_stat['total'] += 1
            if has_attempts:
                priority_stat['attempted'] += 1
            if tier >= 3:  # Mastered
                priority_stat['mastered'] += 1

    return stats




def generate_readme(data, threshold):
    """Generate complete README content.

    Args:
        data: Parsed progress.yaml data
        threshold: Time threshold in minutes for mastery tier

    Returns:
        str: Complete README markdown content
    """
    problems = data.get('problems', {})
    flashcards = data.get('flashcards', {})
    stats = calculate_stats(problems, threshold)

    # Start building README
    lines = [
        '# Python Coding Dojo',
        '',
        'My journey through Elements of Programming Interviews in Python.',
        '',
    ]

    # Add flashcard section
    flashcard_lines = generate_flashcard_section(flashcards)
    if flashcard_lines:
        lines.extend(flashcard_lines)

    # Add goals section (before Overall Progress)
    lines.extend([
        '## Goals',
        '',
        'Progress toward priority-based learning goals.',
        '',
        '| Icon | Tier | Description |',
        '|------|------|-------------|',
        '| ☑️ | Attempted | Problems attempted but not yet solved |',
        '| 👍 | Solved | Problems solved (with or without help) |',
        '| 💪 | Independent | Problems solved without hints or looking at solutions |',
        '| 🏆 | Mastered | Problems solved independently in ≤20 min with optimal solution |',
        '',
    ])

    # Priority emoji mapping
    priority_emoji_map = {
        'P0': '🔴',
        'P1': '🟠',
        'P2': '🟡',
        'P3': '🟢',
        'P4': '🔵'
    }

    # Generate goal progress for each priority level
    for priority in ['P0', 'P1', 'P2', 'P3', 'P4']:
        emoji = priority_emoji_map[priority]
        pstats = stats['priority_stats'][priority]
        total = pstats['total']
        attempted = pstats['attempted']
        mastered = pstats['mastered']

        if total == 0:
            continue  # Skip priorities with no problems

        # Goal 1: Attempt all problems at this priority
        attempt_pct = (attempted / total * 100) if total > 0 else 0
        attempt_complete = attempted == total

        if attempt_complete:
            lines.append('🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟')
        lines.extend([
            f'### {emoji} {priority}: Attempt All ({attempted}/{total} - {attempt_pct:.0f}%)',
            '',
            generate_progress_bar(attempted, total, '☑️'),
            '',
            f"**{attempted} / {total}** problems attempted",
            '',
        ])
        if attempt_complete:
            lines.append('🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟')
        lines.append('')

        # Goal 2: Master all problems at this priority
        master_pct = (mastered / total * 100) if total > 0 else 0
        master_complete = mastered == total

        if master_complete:
            lines.append('🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟')
        lines.extend([
            f'### {emoji} {priority}: Master All ({mastered}/{total} - {master_pct:.0f}%)',
            '',
            generate_progress_bar(mastered, total, '🏆'),
            '',
            f"**{mastered} / {total}** problems mastered",
            '',
        ])
        if master_complete:
            lines.append('🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟🌟')
        lines.append('')

    # Add collapsible Overall Progress section
    lines.extend([
        '<details>',
        '<summary><h2>Overall Progress</h2></summary>',
        '',
    ])

    # Tier 0: Attempted
    tier0_pct = (stats['tier0'] / stats['total'] * 100) if stats['total'] > 0 else 0
    lines.extend([
        '### Tier 0: Attempted ☑️',
        'Problems attempted but not yet solved',
        '',
        generate_progress_bar(stats['tier0'], stats['total'], '☑️'),
        '',
        f"**{stats['tier0']} / {stats['total']}** ({tier0_pct:.1f}%)",
        '',
    ])

    # Tier 1: Solved
    tier1_pct = (stats['tier1'] / stats['total'] * 100) if stats['total'] > 0 else 0
    lines.extend([
        '### Tier 1: Solved 👍',
        'Problems solved (with or without help)',
        '',
        generate_progress_bar(stats['tier1'], stats['total'], '👍'),
        '',
        f"**{stats['tier1']} / {stats['total']}** ({tier1_pct:.1f}%)",
        '',
    ])

    # Tier 2: Independent
    tier2_pct = (stats['tier2'] / stats['total'] * 100) if stats['total'] > 0 else 0
    lines.extend([
        '### Tier 2: Solved Independently 💪',
        'Problems solved without hints or looking at solutions',
        '',
        generate_progress_bar(stats['tier2'], stats['total'], '💪'),
        '',
        f"**{stats['tier2']} / {stats['total']}** ({tier2_pct:.1f}%)",
        '',
    ])

    # Tier 3: Mastered
    tier3_pct = (stats['tier3'] / stats['total'] * 100) if stats['total'] > 0 else 0
    lines.extend([
        '### Tier 3: Mastered 🏆',
        f'Problems solved independently in ≤{threshold} minutes with optimal solution',
        '',
        generate_progress_bar(stats['tier3'], stats['total'], '🏆'),
        '',
        f"**{stats['tier3']} / {stats['total']}** ({tier3_pct:.1f}%)",
        '',
        '</details>',
        '',
    ])

    # Add link to workflow diagrams wiki page
    lines.extend([
        '## Problem-Solving Workflow',
        '',
        'See [Problem-Solving Workflow](wiki/Problem-Solving-Workflow.md) for visual diagrams of the learning approach.',
        '',
    ])

    # Chapter breakdown table (collapsible)
    lines.extend([
        '<details>',
        '<summary><h2>Progress by Chapter</h2></summary>',
        '',
        '| Chapter | Problems | Attempted ☑️ | Solved 👍 | Independent 💪 | Mastered 🏆 |',
        '|---------|----------|-------------|--------|---------------|-------------|',
    ])

    # Sort chapters by chapter number
    # EPI (numeric), Practical (P1-P6), Trading (T1), ML (M1-M5)
    def chapter_sort_key(item):
        chapter_num = item[1]['chapter_num']
        if chapter_num.isdigit():
            return (0, int(chapter_num), '')  # EPI chapters first
        elif chapter_num.startswith('P'):
            return (1, int(chapter_num[1:]), '')  # Practical chapters second
        elif chapter_num.startswith('T'):
            return (2, int(chapter_num[1:]), '')  # Trading chapters third
        elif chapter_num.startswith('M'):
            return (3, int(chapter_num[1:]), '')  # ML chapters fourth
        else:
            return (4, 0, chapter_num)  # Other chapters last

    sorted_chapters = sorted(stats['chapters'].items(), key=chapter_sort_key)

    for chapter_name, chapter_stats in sorted_chapters:
        chapter_num = chapter_stats['chapter_num']
        total = chapter_stats['total']
        tier0 = chapter_stats['tier0']
        tier1 = chapter_stats['tier1']
        tier2 = chapter_stats['tier2']
        tier3 = chapter_stats['tier3']

        tier0_pct = (tier0 / total * 100) if total > 0 else 0
        tier1_pct = (tier1 / total * 100) if total > 0 else 0
        tier2_pct = (tier2 / total * 100) if total > 0 else 0
        tier3_pct = (tier3 / total * 100) if total > 0 else 0

        lines.append(
            f'| {chapter_num}: {chapter_name} | {total} | '
            f'{tier0} ({tier0_pct:.0f}%) | '
            f'{tier1} ({tier1_pct:.0f}%) | '
            f'{tier2} ({tier2_pct:.0f}%) | '
            f'{tier3} ({tier3_pct:.0f}%) |'
        )

    # Total row
    tier0_pct = (stats['tier0'] / stats['total'] * 100) if stats['total'] > 0 else 0
    tier1_pct = (stats['tier1'] / stats['total'] * 100) if stats['total'] > 0 else 0
    tier2_pct = (stats['tier2'] / stats['total'] * 100) if stats['total'] > 0 else 0
    tier3_pct = (stats['tier3'] / stats['total'] * 100) if stats['total'] > 0 else 0

    lines.append(
        f"| **Total** | **{stats['total']}** | "
        f"**{stats['tier0']}** | "
        f"**{stats['tier1']}** | "
        f"**{stats['tier2']}** | "
        f"**{stats['tier3']}** |"
    )

    lines.extend([
        '',
        '</details>',
        '',
        '## All Problems',
        '',
    ])

    # Group problems by chapter for detailed listing
    problems_by_chapter = defaultdict(list)
    for problem_id, problem_info in stats['problems_by_tier'].items():
        chapter_name = problem_info['metadata'].get('chapter_name', 'Unknown')
        problems_by_chapter[chapter_name].append((problem_id, problem_info))

    # Sort chapters and problems
    for chapter_name, chapter_stats in sorted_chapters:
        chapter_num = chapter_stats['chapter_num']
        lines.extend([
            f'### Chapter {chapter_num}: {chapter_name}',
            '',
            '| # | Problem | Priority | LeetCode | Difficulty | Status | Best Time |',
            '|---|---------|----------|----------|------------|--------|-----------|',
        ])

        # Get problems for this chapter and sort by problem number
        chapter_problems = problems_by_chapter.get(chapter_name, [])
        chapter_problems.sort(key=lambda x: x[1]['metadata'].get('problem_number', ''))

        for problem_id, problem_info in chapter_problems:
            metadata = problem_info['metadata']
            tier = problem_info['tier']
            best_time = problem_info['best_time']
            has_attempts = problem_info['has_attempts']

            problem_num = metadata.get('problem_number', '')
            problem_name = metadata.get('name', problem_id)

            # Skip bootcamp problems (problem numbers ending in .00)
            if problem_num.endswith('.00'):
                continue

            # Get priority for this problem (from metadata) and map to emoji
            priority_str = metadata.get('priority', '')
            priority_emoji_map = {
                'P0': '🔴',
                'P1': '🟠',
                'P2': '🟡',
                'P3': '🟢',
                'P4': '🔵'
            }
            priority = priority_emoji_map.get(priority_str, '')

            # Determine status icon
            if tier == 0 and not has_attempts:
                status = ''
            elif tier == 0 and has_attempts:
                status = '☑️'
            elif tier == 1:
                status = '👍'
            elif tier == 2:
                status = '💪'
            else:  # tier == 3
                status = '🏆'

            # Show best time only for tier 2+
            time_str = ''
            if tier >= 2 and best_time is not None:
                time_str = f'{best_time} min'

            # Get LeetCode info
            lc_num = metadata.get('leetcode_num', '')
            lc_name = metadata.get('leetcode_name', '')
            lc_difficulty = metadata.get('leetcode_difficulty', '')

            # Format LeetCode as clickable link
            if lc_num and lc_name:
                # Convert name to URL slug (lowercase, spaces to hyphens)
                lc_slug = lc_name.lower().replace(' ', '-').replace('(', '').replace(')', '').replace(',', '')
                lc_link = f'[#{lc_num}](https://leetcode.com/problems/{lc_slug}/)'
            else:
                lc_link = ''

            lines.append(f'| {problem_num} | {problem_name} | {priority} | {lc_link} | {lc_difficulty} | {status} | {time_str} |')

        lines.extend(['', '---', ''])

    # Add timestamp
    today = datetime.now().strftime('%Y-%m-%d')
    lines.extend(['', f'*Last updated: {today}*', ''])

    return '\n'.join(lines)


@click.command()
@click.option('--threshold', default=20, type=int,
              help='Time threshold in minutes for mastery tier (default: 20)')
@click.option('--output', default='README.md',
              help='Output file path (default: README.md)')
def main(threshold, output):
    """Generate README.md from progress.yaml.

    Analyzes all problem attempts and generates a comprehensive README with:
    - Four-tier emoji progress bars (☑️ → 👍 → 💪 → 🏆)
    - Chapter-by-chapter statistics
    - Complete problem list with status icons
    """
    repo_root = Path(__file__).parent.parent
    progress_file = repo_root / 'progress.yaml'
    output_file = repo_root / output

    if not progress_file.exists():
        click.echo(f"Error: {progress_file} not found", err=True)
        return 1

    # Load progress data
    click.echo(f"Reading progress from {progress_file}...")
    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    # Generate README
    click.echo(f"Generating README (mastery threshold: {threshold} minutes)...")
    readme_content = generate_readme(data, threshold)

    # Write output
    with open(output_file, 'w') as f:
        f.write(readme_content)

    click.echo(f"☑️ Generated {output_file}")

    # Show summary
    problems = data.get('problems', {})
    stats = calculate_stats(problems, threshold)
    click.echo(f"\nProgress Summary:")
    click.echo(f"  Attempted: {stats['tier0']} / {stats['total']}")
    click.echo(f"  Solved: {stats['tier1']} / {stats['total']}")
    click.echo(f"  Independent: {stats['tier2']} / {stats['total']}")
    click.echo(f"  Mastered: {stats['tier3']} / {stats['total']}")

    return 0


if __name__ == '__main__':
    main()
