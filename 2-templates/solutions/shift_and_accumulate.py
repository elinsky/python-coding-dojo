import sys
import os

# Add 3-problems to path to import test_framework
sys.path.insert(0, os.path.join(os.path.dirname(__file__), '..', '..', '3-problems'))

from test_framework import generic_test


def power(x: float, y: int) -> float:
    """
    Template: Shift-and-Conditional-Accumulate

    Problem: Given base x and exponent y, return x^y

    Strategy: Process each bit of exponent; if bit is 1, multiply result by current power;
              square the current power each iteration

    Pattern structure:
        result = 1.0
        current_power = x
        while y:
            if y & 1:
                result *= current_power
            current_power *= current_power
            y >>= 1
        return result

    Patterns used:
    - Shift-and-Conditional-Accumulate

    Memory hook: "Selector shrinks right, value grows by squaring"

    Time complexity: O(log y)
    Space complexity: O(1)
    """
    result = 1.0
    power_val = y

    # Handle negative exponents
    if y < 0:
        power_val = -y
        x = 1.0 / x

    while power_val:
        if power_val & 1:  # Check LSB of exponent
            result *= x
        x *= x  # Square the base
        power_val >>= 1  # Move to next bit

    return result


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('shift_and_accumulate.py',
                                       'shift_and_accumulate.tsv',
                                       power))
