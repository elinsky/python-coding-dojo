# Python Coding Dojo

Personal progress tracking system for Elements of Programming Interviews in Python.

## Key Commands

- **log-attempt**: Log problem attempts (use via Claude skill for natural language)
- **update-readme**: Regenerate README.md from progress.yaml
- **generate-problems**: Regenerate problem metadata from problem_mapping.js

## Progress System

Three-tier progression tracked in `progress.yaml`:
- **Tier 1 (👍)**: Solved (with or without help)
- **Tier 2 (💪)**: Independent (no hints, no solution)
- **Tier 3 (🏆)**: Mastered (independent + ≤20 min + optimal solution)

"Optimal" means correct time/space complexity matching the book's solution.

## Workflow

1. Solve problems in `epi_judge_python/`
2. Log attempts: "log <problem_id> - <time>min, <tries> tries, solved/not solved, used hints/no hints"
3. Update README: `~/.pyenv/versions/python-coding-dojo/bin/python scripts/update_readme.py`

## Notes

- 213 total problems across 16 chapters
- Best times only shown for independent solutions (Tier 2+)
- Multiple independent attempts still count as independent
- Virtual env: python-coding-dojo (Python 3.11.11)
