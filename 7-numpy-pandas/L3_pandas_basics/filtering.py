"""
Filtering

Problem P1.05 - P1.06
"""
import pandas as pd


def filter_by_conditions(df: pd.DataFrame) -> pd.DataFrame:
    """
    P1.05: Select all rows where age > 30 AND city == "Chicago".

    Args:
        df: DataFrame with 'age' and 'city' columns

    Returns:
        pd.DataFrame: Filtered rows
    """
    # TODO - you fill in here
    pass


def unique_value_counts(df: pd.DataFrame, column: str) -> pd.Series:
    """
    P1.06: Find unique values and their counts in a column.

    Args:
        df: DataFrame
        column: Column name to analyze

    Returns:
        pd.Series: Value counts (index = unique values, values = counts)
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P1.05
    df = pd.DataFrame({
        'name': ['Alice', 'Bob', 'Charlie', 'Diana', 'Eve'],
        'age': [25, 35, 40, 28, 45],
        'city': ['NYC', 'Chicago', 'Chicago', 'LA', 'Chicago']
    })
    result = filter_by_conditions(df)
    assert result is not None, "P1.05: Function returned None"
    assert len(result) == 2, f"P1.05: Expected 2 rows, got {len(result)}"
    assert set(result['name']) == {'Charlie', 'Eve'}, "P1.05: Wrong rows selected"
    print("P1.05 filter_by_conditions: PASSED")

    # Test P1.06
    df = pd.DataFrame({'fruit': ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']})
    result = unique_value_counts(df, 'fruit')
    assert result is not None, "P1.06: Function returned None"
    assert isinstance(result, pd.Series), "P1.06: Should return a Series"
    assert result['apple'] == 3, "P1.06: apple count should be 3"
    assert result['banana'] == 2, "P1.06: banana count should be 2"
    assert result['cherry'] == 1, "P1.06: cherry count should be 1"
    print("P1.06 unique_value_counts: PASSED")

    print("\nAll filtering tests passed!")
