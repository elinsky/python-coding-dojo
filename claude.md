# Python Coding Dojo

Personal progress tracking system for coding interview practice.

## Problem Categories

| Directory | Prefix | Description |
|-----------|--------|-------------|
| `3-problems/` | 4.xx - 24.xx | EPI algorithmic problems (204) |
| `4-practical/` | P1.xx - P6.xx | Practical file/data problems (6) |
| `5-trading/` | T1.xx | Trading/quant problems (12) |

## Key Commands

- **log-attempt**: Log problem attempts (use via Claude skill for natural language)
- **update-readme**: Regenerate README.md from progress.yaml

## Progress System

Three-tier progression tracked in `progress.yaml`:
- **Tier 1 (👍)**: Solved (with or without help)
- **Tier 2 (💪)**: Independent (no hints, no solution)
- **Tier 3 (🏆)**: Mastered (independent + ≤20 min + optimal solution)

"Optimal" means correct time/space complexity matching the book's solution.

## Workflow

### EPI Problems
1. Solve problems in `3-problems/`
2. Log attempts: "log <problem_id> - <time>min, <tries> tries, solved/not solved, used hints/no hints"
3. Update README: `~/.pyenv/versions/python-coding-dojo/bin/python scripts/update_readme.py`

### Practical/Trading Problems
1. Solve problems in `4-practical/` or `5-trading/`
2. Run tests: `~/.pyenv/versions/python-coding-dojo/bin/python <problem>.py`
3. Log attempts same as EPI

## Notes

- 222 total problems (excluding bootcamp)
- Best times only shown for independent solutions (Tier 2+)
- Virtual env: python-coding-dojo (Python 3.11.11)
