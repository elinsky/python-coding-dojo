"""
DataFrame Creation

Problem P1.01 - P1.02
"""
import pandas as pd
import numpy as np


def create_df_from_dict() -> pd.DataFrame:
    """
    P1.01: Create a DataFrame from a dictionary of lists.

    Create a DataFrame with these columns and values:
        name: ["Alice", "Bob", "Charlie"]
        age: [25, 30, 35]
        city: ["NYC", "LA", "Chicago"]

    Returns:
        pd.DataFrame: DataFrame with 3 rows and 3 columns
    """
    # TODO - you fill in here
    pass


def explore_dataframe(df: pd.DataFrame) -> dict:
    """
    P1.02: Explore a DataFrame and return summary info.

    Return a dictionary with:
        - 'head': first 5 rows (as DataFrame)
        - 'dtypes': column dtypes (as Series)
        - 'missing_counts': count of missing values per column (as Series)

    Args:
        df: Input DataFrame

    Returns:
        dict with keys 'head', 'dtypes', 'missing_counts'
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P1.01
    result = create_df_from_dict()
    assert result is not None, "P1.01: Function returned None"
    assert isinstance(result, pd.DataFrame), "P1.01: Should return a DataFrame"
    assert list(result.columns) == ['name', 'age', 'city'], f"P1.01: Wrong columns: {list(result.columns)}"
    assert len(result) == 3, f"P1.01: Expected 3 rows, got {len(result)}"
    assert result['name'].tolist() == ["Alice", "Bob", "Charlie"], "P1.01: Wrong name values"
    print("P1.01 create_df_from_dict: PASSED")

    # Test P1.02
    test_df = pd.DataFrame({
        'A': [1, 2, np.nan, 4, 5],
        'B': ['a', 'b', 'c', None, 'e'],
        'C': [1.0, 2.0, 3.0, 4.0, 5.0]
    })
    result = explore_dataframe(test_df)
    assert result is not None, "P1.02: Function returned None"
    assert 'head' in result, "P1.02: Missing 'head' key"
    assert 'dtypes' in result, "P1.02: Missing 'dtypes' key"
    assert 'missing_counts' in result, "P1.02: Missing 'missing_counts' key"
    assert len(result['head']) == 5, "P1.02: head should have 5 rows"
    assert result['missing_counts']['A'] == 1, "P1.02: Column A has 1 missing value"
    assert result['missing_counts']['B'] == 1, "P1.02: Column B has 1 missing value"
    print("P1.02 explore_dataframe: PASSED")

    print("\nAll DataFrame creation tests passed!")
