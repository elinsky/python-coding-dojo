#!/usr/bin/env python3
"""Generate problem metadata from problem_mapping.js and epi_judge_python directory."""

import json
import re
from pathlib import Path
import yaml


def parse_problem_mapping_js(mapping_file: Path) -> dict:
    """Parse problem_mapping.js file into a Python dict."""
    with open(mapping_file, 'r') as f:
        content = f.read()

    # Remove JavaScript variable assignment
    json_str = content.replace('problem_mapping = ', '').rstrip(';')
    return json.loads(json_str)


def extract_problem_id(filename: str) -> str:
    """Extract problem ID from filename (e.g., count_bits.py -> count_bits)."""
    return Path(filename).stem


def generate_metadata(repo_root: Path) -> dict:
    """Generate problem metadata from problem_mapping.js and filesystem."""

    # Parse problem_mapping.js
    mapping_file = repo_root / 'problem_mapping.js'
    if not mapping_file.exists():
        raise FileNotFoundError(f"Could not find {mapping_file}")

    problem_data = parse_problem_mapping_js(mapping_file)

    problems = {}

    # Iterate through chapters
    for chapter_full_name, chapter_problems in problem_data.items():
        # Extract chapter number (e.g., "Chapter 04: Primitive Types" -> "04")
        chapter_match = re.match(r'Chapter (\d+):\s*(.+)', chapter_full_name)
        if not chapter_match:
            continue

        chapter_num = chapter_match.group(1)
        chapter_name = chapter_match.group(2)

        # Iterate through problems in chapter
        for problem_full_name, language_data in chapter_problems.items():
            # Extract problem number (e.g., "4.01 Computing the parity" -> "4.01")
            problem_match = re.match(r'([\d.]+)\s+(.+)', problem_full_name)
            if not problem_match:
                continue

            problem_number = problem_match.group(1)
            problem_name = problem_match.group(2)

            # Get Python file info
            python_key = next((k for k in language_data.keys() if k.startswith('Python:')), None)
            if not python_key:
                continue

            python_file = python_key.split('Python: ')[1]
            problem_id = extract_problem_id(python_file)

            # Verify file exists
            file_path = repo_root / '3-problems' / python_file
            if not file_path.exists():
                print(f"Warning: File not found: {file_path}")
                continue

            # Add to problems dict
            problems[problem_id] = {
                'file': f'3-problems/{python_file}',
                'chapter': f'{chapter_num.lower()}_' + chapter_name.lower().replace(' ', '_').replace('-', '_'),
                'chapter_name': chapter_name,
                'problem_number': problem_number,
                'name': problem_name,
                'attempts': []
            }

    return problems


def main():
    """Main entry point."""
    repo_root = Path(__file__).parent.parent
    progress_file = repo_root / 'progress.yaml'

    print(f"Generating problem metadata...")
    print(f"Repository root: {repo_root}")

    # Generate metadata
    problems = generate_metadata(repo_root)

    print(f"Found {len(problems)} Python problems")

    # Load existing progress if it exists
    existing_data = {'problems': {}}
    if progress_file.exists():
        with open(progress_file, 'r') as f:
            existing_data = yaml.safe_load(f) or {'problems': {}}

    # Merge: keep existing attempts, update metadata
    for problem_id, metadata in problems.items():
        if problem_id in existing_data['problems']:
            # Keep existing attempts
            metadata['attempts'] = existing_data['problems'][problem_id].get('attempts', [])
        existing_data['problems'][problem_id] = metadata

    # Write to progress.yaml
    with open(progress_file, 'w') as f:
        yaml.dump(existing_data, f, default_flow_style=False, sort_keys=True)

    print(f"✓ Wrote metadata to {progress_file}")
    print(f"\nSample problems:")
    for i, (problem_id, data) in enumerate(list(problems.items())[:3]):
        print(f"  - {problem_id}: {data['name']}")

    print(f"\nYou can now delete problem_mapping.js if you want!")


if __name__ == '__main__':
    main()
