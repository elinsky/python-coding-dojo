---
name: flashcard-drill
description: Run timed flashcard drills when user says "drill <category>" (e.g., "drill bitwise", "drill 1-bitwise", "drill arrays"). Reads all flashcards upfront, quizzes rapidly, logs results, drills missed cards, then updates README.
---

# Flashcard Drill

Run a timed flashcard drill session for a category in `0-operations/`.

## Workflow

### 1. Setup (before starting)
- Read ALL flashcard files from the requested category directory
- Each `.md` file is one flashcard: the H1 heading is the question, the code block is the answer
- Tell the user the count and that you're ready
- User will say "go" or similar to start

### 2. Quiz Phase (be FAST)
- Present questions one at a time (just the H1 heading text)
- When user answers, respond IMMEDIATELY with:
  - "Correct!" or "Wrong - [correct answer]"
  - Then the next question in the SAME response
- NO extra commentary, NO thinking, NO explanations during the drill
- Track: correct count, incorrect cards (for later review)

### 3. Log Results
After the last card, ask the user for their time in seconds, then run:

```bash
~/.pyenv/versions/python-coding-dojo/bin/python scripts/log_flashcard_drill.py <category> --score <correct> --count <total> --time <seconds> --notes "Missed: Q3, Q7, Q12"
```

**IMPORTANT**: Always include `--notes` with the list of missed question numbers (e.g., "Missed: Q3, Q7, Q12"). Use the question number from the filename (e.g., `03-clear-bit.md` = Q3).

Category names in progress.yaml:
- `bitwise` (for 1-bitwise)
- `arrays` (for 2-arrays)
- `strings` (for 3-strings)
- `linked-lists` (for 4-linked-lists)
- `stacks-queues` (for 5-stacks-queues)
- `binary-trees` (for 6-binary-trees)
- `heaps` (for 7-heaps)
- `searching` (for 8-searching)
- `hash-tables` (for 12-hash-tables)
- `sorting` (for 13-sorting)
- `bst` (for 14-bst)
- `recursion` (for 15-recursion)
- `dynamic-programming` (for 16-dynamic-programming)
- `greedy-invariants` (for 17-greedy-invariants)
- `graphs` (for 18-graphs)

### 4. Review Missed Cards
If any cards were missed, offer to drill them again. Repeat until user is satisfied.

### 5. Finish
```bash
~/.pyenv/versions/python-coding-dojo/bin/python scripts/update_readme.py
```

Then commit and push (no "Claude" in commit message):
```bash
git add -A && git commit -m "Log flashcard drill: <category>" && git push
```

## Scoring Rules

From `log_flashcard_drill.py`:
- **Pass**: Perfect score (score == count) AND under target time
- **Fail**: Any wrong answers OR over target time

## Flashcard Format

Each `.md` file in `0-operations/<category>/`:
```markdown
# Question text here?

\`\`\`python
answer_code_here
\`\`\`
```

## Example Session

User: "drill bitwise"
Claude: *reads all 17 files in 0-operations/1-bitwise/*
Claude: "Ready! 17 cards. Say 'go' when ready."
User: "go"
Claude: "How do you get bit at position i?"
User: "(x >> i) & 1"
Claude: "Correct! How do you set bit at position i?"
...
Claude: "Done! 16/17 correct. What was your time in seconds?"
User: "485"
Claude: *logs attempt with --notes "Missed: Q5"*
Claude: *offers to drill missed card*
