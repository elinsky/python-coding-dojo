#!/usr/bin/env python3
"""Log a flashcard drill attempt to progress.yaml."""

from datetime import datetime
from pathlib import Path
import yaml
import click


def format_time(seconds):
    """Format seconds as m:ss."""
    minutes = seconds // 60
    secs = seconds % 60
    return f"{minutes}:{secs:02d}"


@click.command()
@click.argument('category')
@click.option('--score', type=int, required=True,
              help='Number of cards answered correctly')
@click.option('--count', type=int, required=True,
              help='Total number of cards in the drill')
@click.option('--time', 'time_seconds', type=int, required=True,
              help='Time taken in seconds')
def main(category, score, count, time_seconds):
    """Log a flashcard drill attempt for CATEGORY to progress.yaml.

    Example:
        log-flashcard-drill bitwise --score 17 --count 17 --time 480
    """
    repo_root = Path(__file__).parent.parent
    progress_file = repo_root / 'progress.yaml'

    if not progress_file.exists():
        click.echo(f"Error: {progress_file} not found.", err=True)
        return 1

    # Load progress.yaml
    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    # Ensure flashcards section exists
    if 'flashcards' not in data:
        data['flashcards'] = {}

    # Validate category exists
    if category not in data['flashcards']:
        click.echo(f"Error: Category '{category}' not found in progress.yaml", err=True)
        click.echo(f"\nAvailable categories:", err=True)
        for cat in data.get('flashcards', {}).keys():
            click.echo(f"  - {cat}", err=True)
        return 1

    # Create attempt entry
    attempt = {
        'date': datetime.now().isoformat(),
        'count': count,
        'score': score,
        'time_seconds': time_seconds,
    }

    # Add attempt to category (prepend so most recent is first)
    if 'attempts' not in data['flashcards'][category]:
        data['flashcards'][category]['attempts'] = []

    data['flashcards'][category]['attempts'].insert(0, attempt)

    # Write back to file
    with open(progress_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=True)

    # Print confirmation
    category_name = data['flashcards'][category].get('name', category)
    target_seconds = data['flashcards'][category].get('target_seconds')

    click.echo(f"✓ Logged drill for: {category} ({category_name})")
    click.echo(f"  Score: {score}/{count}")
    click.echo(f"  Time: {format_time(time_seconds)}")

    # Show pass/fail status if target is defined
    if target_seconds:
        passed = (score == count) and (time_seconds <= target_seconds)
        status = "✅ PASS" if passed else "⬜ Not yet"
        click.echo(f"  Target: {format_time(target_seconds)}")
        click.echo(f"  Status: {status}")

    # Show total attempts for this category
    total_attempts = len(data['flashcards'][category]['attempts'])
    click.echo(f"\nTotal drills for this category: {total_attempts}")

    return 0


if __name__ == '__main__':
    main()
