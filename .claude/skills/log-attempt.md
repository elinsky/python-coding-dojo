# Log Problem Attempt

Log an attempt for a coding problem to track progress.

## Usage

The user will tell you about a problem attempt in natural language. Parse their input and call the log-attempt script.

Examples of user input:
- "log count_bits - 15 min, 3 tries, solved, used hints"
- "log parity solved, 1 try, no hints, 8 minutes"
- "log swap_bits, didn't solve it, looked at solution"
- "log reverse_bits - 22min, solved, no hints, no solution"

## Instructions

1. Parse the user's input to extract:
   - problem_id (required)
   - time_minutes (optional)
   - submissions/tries (optional, defaults to 1 if solved)
   - solved (default: true)
   - used_hints (default: false)
   - used_solution (default: false)
   - notes (optional)

2. Call the log-attempt script with appropriate flags:
   ```bash
   ~/.pyenv/versions/python-coding-dojo/bin/python scripts/log_attempt.py <problem_id> [OPTIONS]
   ```

3. Show the output to the user

## Options

- `--time MINUTES` - Time taken in minutes
- `--submissions N` - Number of attempts until correct
- `--solved` or `--no-solved` - Whether solved (default: --solved)
- `--used-hints` or `--no-used-hints` - Whether used hints (default: --no-used-hints)
- `--used-solution` or `--no-used-solution` - Whether looked at solution (default: --no-used-solution)
- `--notes "text"` - Optional notes

## Parsing hints

- "tries", "attempts", "submissions" all mean `--submissions`
- "hint", "hints" means `--used-hints`
- "solution", "looked at solution" means `--used-solution`
- "didn't solve", "not solved", "gave up" means `--no-solved`
- "min", "minutes" indicates time
- Default to solved=true unless explicitly stated otherwise

## Examples

User: "log count_bits - 15 min, 3 tries, solved, used hints"
```bash
~/.pyenv/versions/python-coding-dojo/bin/python scripts/log_attempt.py count_bits --time 15 --submissions 3 --solved --used-hints
```

User: "log parity, didn't solve, looked at solution"
```bash
~/.pyenv/versions/python-coding-dojo/bin/python scripts/log_attempt.py parity --no-solved --used-solution
```

User: "log swap_bits - first try, 8 minutes, no hints"
```bash
~/.pyenv/versions/python-coding-dojo/bin/python scripts/log_attempt.py swap_bits --time 8 --submissions 1 --solved --no-used-hints --no-used-solution
```
