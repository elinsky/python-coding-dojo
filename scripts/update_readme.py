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
        tuple: (tier, best_time)
            tier: 0 (unsolved), 1 (solved), 2 (independent), 3 (mastered)
            best_time: minimum time in minutes for tier 2+ attempts, None otherwise
    """
    attempts = problem_data.get('attempts', [])

    if not attempts:
        return 0, None

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

    return tier, best_time


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
            'tier1': int,
            'tier2': int,
            'tier3': int,
            'total': int,
            'chapters': {
                chapter_name: {
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
                    'metadata': dict
                }
            }
        }
    """
    stats = {
        'tier1': 0,
        'tier2': 0,
        'tier3': 0,
        'total': len(problems),
        'chapters': defaultdict(lambda: {'tier1': 0, 'tier2': 0, 'tier3': 0, 'total': 0, 'chapter_num': ''}),
        'problems_by_tier': {}
    }

    for problem_id, problem_data in problems.items():
        tier, best_time = analyze_problem(problem_data, threshold)

        # Store problem analysis
        stats['problems_by_tier'][problem_id] = {
            'tier': tier,
            'best_time': best_time,
            'metadata': problem_data
        }

        # Update overall stats
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

        if tier >= 1:
            chapter_stats['tier1'] += 1
        if tier >= 2:
            chapter_stats['tier2'] += 1
        if tier >= 3:
            chapter_stats['tier3'] += 1

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
    stats = calculate_stats(problems, threshold)

    # Start building README
    lines = [
        '# Python Coding Dojo',
        '',
        'My journey through Elements of Programming Interviews in Python.',
        '',
        '## Overall Progress',
        '',
    ]

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
    ])

    # Chapter breakdown table
    lines.extend([
        '## Progress by Chapter',
        '',
        '| Chapter | Problems | Solved | Independent ⭐ | Mastered 🏆 |',
        '|---------|----------|--------|---------------|-------------|',
    ])

    # Sort chapters by chapter number
    sorted_chapters = sorted(
        stats['chapters'].items(),
        key=lambda x: x[1]['chapter_num']
    )

    for chapter_name, chapter_stats in sorted_chapters:
        chapter_num = chapter_stats['chapter_num']
        total = chapter_stats['total']
        tier1 = chapter_stats['tier1']
        tier2 = chapter_stats['tier2']
        tier3 = chapter_stats['tier3']

        tier1_pct = (tier1 / total * 100) if total > 0 else 0
        tier2_pct = (tier2 / total * 100) if total > 0 else 0
        tier3_pct = (tier3 / total * 100) if total > 0 else 0

        lines.append(
            f'| {chapter_num}: {chapter_name} | {total} | '
            f'{tier1} ({tier1_pct:.0f}%) | '
            f'{tier2} ({tier2_pct:.0f}%) | '
            f'{tier3} ({tier3_pct:.0f}%) |'
        )

    # Total row
    tier1_pct = (stats['tier1'] / stats['total'] * 100) if stats['total'] > 0 else 0
    tier2_pct = (stats['tier2'] / stats['total'] * 100) if stats['total'] > 0 else 0
    tier3_pct = (stats['tier3'] / stats['total'] * 100) if stats['total'] > 0 else 0

    lines.append(
        f"| **Total** | **{stats['total']}** | "
        f"**{stats['tier1']}** | "
        f"**{stats['tier2']}** | "
        f"**{stats['tier3']}** |"
    )

    lines.extend(['', '## All Problems', ''])

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
            '| # | Problem | Status | Best Time |',
            '|---|---------|--------|-----------|',
        ])

        # Get problems for this chapter and sort by problem number
        chapter_problems = problems_by_chapter.get(chapter_name, [])
        chapter_problems.sort(key=lambda x: x[1]['metadata'].get('problem_number', ''))

        for problem_id, problem_info in chapter_problems:
            metadata = problem_info['metadata']
            tier = problem_info['tier']
            best_time = problem_info['best_time']

            problem_num = metadata.get('problem_number', '')
            problem_name = metadata.get('name', problem_id)

            # Determine status icon
            if tier == 0:
                status = ''
            elif tier == 1:
                status = '✓'
            elif tier == 2:
                status = '⭐'
            else:  # tier == 3
                status = '🏆'

            # Show best time only for tier 2+
            time_str = ''
            if tier >= 2 and best_time is not None:
                time_str = f'{best_time} min'

            lines.append(f'| {problem_num} | {problem_name} | {status} | {time_str} |')

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
    - Three-tier emoji progress bars (👍 → 💪 → 🏆)
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

    click.echo(f"✓ Generated {output_file}")

    # Show summary
    problems = data.get('problems', {})
    stats = calculate_stats(problems, threshold)
    click.echo(f"\nProgress Summary:")
    click.echo(f"  Solved: {stats['tier1']} / {stats['total']}")
    click.echo(f"  Independent: {stats['tier2']} / {stats['total']}")
    click.echo(f"  Mastered: {stats['tier3']} / {stats['total']}")

    return 0


if __name__ == '__main__':
    main()
