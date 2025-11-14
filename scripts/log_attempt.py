#!/usr/bin/env python3
"""Log a problem attempt to progress.yaml."""

from datetime import datetime
from pathlib import Path
import yaml
import click


@click.command()
@click.argument('problem_id')
@click.option('--time', 'time_minutes', type=int, default=None,
              help='Time taken in minutes')
@click.option('--submissions', type=int, default=None,
              help='Number of submissions/attempts until correct')
@click.option('--solved/--no-solved', default=True,
              help='Whether you solved the problem')
@click.option('--used-hints/--no-used-hints', 'used_hints', default=False,
              help='Whether you used hints')
@click.option('--used-solution/--no-used-solution', 'used_solution', default=False,
              help='Whether you looked at the solution')
@click.option('--optimal/--no-optimal', 'optimal', default=False,
              help='Whether the solution is optimal (correct complexity)')
@click.option('--notes', default='', help='Optional notes about the attempt')
def main(problem_id, time_minutes, submissions, solved, used_hints, used_solution, optimal, notes):
    """Log an attempt for PROBLEM_ID to progress.yaml.

    Example:
        log-attempt count_bits --time 15 --submissions 3 --solved --used-hints
    """
    repo_root = Path(__file__).parent.parent
    progress_file = repo_root / 'progress.yaml'

    if not progress_file.exists():
        click.echo(f"Error: {progress_file} not found. Run generate-problems first.", err=True)
        return 1

    # Load progress.yaml
    with open(progress_file, 'r') as f:
        data = yaml.safe_load(f)

    # Validate problem exists
    if problem_id not in data.get('problems', {}):
        click.echo(f"Error: Problem '{problem_id}' not found in progress.yaml", err=True)
        click.echo(f"\nDid you mean one of these?", err=True)
        similar = [p for p in data['problems'].keys() if problem_id in p]
        for p in similar[:5]:
            click.echo(f"  - {p}", err=True)
        return 1

    # Default submissions to 1 if solved
    if submissions is None and solved:
        submissions = 1

    # Create attempt entry
    attempt = {
        'date': datetime.now().isoformat(),
        'time_minutes': time_minutes,
        'submissions': submissions,
        'solved': solved,
        'used_hints': used_hints,
        'used_solution': used_solution,
        'optimal': optimal,
    }

    if notes:
        attempt['notes'] = notes

    # Add attempt to problem
    if 'attempts' not in data['problems'][problem_id]:
        data['problems'][problem_id]['attempts'] = []

    data['problems'][problem_id]['attempts'].append(attempt)

    # Write back to file
    with open(progress_file, 'w') as f:
        yaml.dump(data, f, default_flow_style=False, sort_keys=True)

    # Print confirmation
    problem_name = data['problems'][problem_id]['name']
    click.echo(f"✓ Logged attempt for: {problem_id} ({problem_name})")
    click.echo(f"  Solved: {solved}")
    if time_minutes:
        click.echo(f"  Time: {time_minutes} min")
    if submissions:
        click.echo(f"  Submissions: {submissions}")
    if used_hints:
        click.echo(f"  Used hints: yes")
    if used_solution:
        click.echo(f"  Used solution: yes")
    if optimal:
        click.echo(f"  Optimal: yes")
    if notes:
        click.echo(f"  Notes: {notes}")

    # Show total attempts for this problem
    total_attempts = len(data['problems'][problem_id]['attempts'])
    click.echo(f"\nTotal attempts for this problem: {total_attempts}")

    return 0


if __name__ == '__main__':
    main()
