"""
Reshaping

Problem P2.04 - P2.05
"""
import pandas as pd


def wide_to_long(df: pd.DataFrame, id_col: str, value_vars: list) -> pd.DataFrame:
    """
    P2.04: Convert a DataFrame from wide to long format using melt.

    Example:
        Wide:  id | Jan | Feb | Mar
               1  | 10  | 20  | 30

        Long:  id | month | value
               1  | Jan   | 10
               1  | Feb   | 20
               1  | Mar   | 30

    Args:
        df: Wide format DataFrame
        id_col: Column to use as identifier
        value_vars: Columns to unpivot

    Returns:
        pd.DataFrame: Long format DataFrame with columns [id_col, 'variable', 'value']
    """
    # TODO - you fill in here
    pass


def pivot_mean_sales(df: pd.DataFrame) -> pd.DataFrame:
    """
    P2.05: Pivot to compute the mean sales per product per month.

    Args:
        df: DataFrame with columns ['product', 'month', 'sales']

    Returns:
        pd.DataFrame: Pivoted with products as rows, months as columns, mean sales as values
    """
    # TODO - you fill in here
    pass


# ============ Tests ============
if __name__ == '__main__':
    # Test P2.04
    df = pd.DataFrame({
        'id': [1, 2],
        'Jan': [10, 40],
        'Feb': [20, 50],
        'Mar': [30, 60]
    })
    result = wide_to_long(df, 'id', ['Jan', 'Feb', 'Mar'])
    assert result is not None, "P2.04: Function returned None"
    assert len(result) == 6, f"P2.04: Expected 6 rows, got {len(result)}"
    assert 'variable' in result.columns, "P2.04: Should have 'variable' column"
    assert 'value' in result.columns, "P2.04: Should have 'value' column"
    print("P2.04 wide_to_long: PASSED")

    # Test P2.05
    df = pd.DataFrame({
        'product': ['A', 'A', 'B', 'B', 'A', 'B'],
        'month': ['Jan', 'Feb', 'Jan', 'Feb', 'Jan', 'Jan'],
        'sales': [100, 150, 200, 250, 120, 180]
    })
    result = pivot_mean_sales(df)
    assert result is not None, "P2.05: Function returned None"
    # A in Jan: mean(100, 120) = 110
    assert result.loc['A', 'Jan'] == 110, f"P2.05: A/Jan should be 110"
    # B in Jan: mean(200, 180) = 190
    assert result.loc['B', 'Jan'] == 190, f"P2.05: B/Jan should be 190"
    print("P2.05 pivot_mean_sales: PASSED")

    print("\nAll reshaping tests passed!")
