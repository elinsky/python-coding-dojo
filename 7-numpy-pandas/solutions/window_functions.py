"""Solution for Window Functions"""
import pandas as pd


def rolling_average_7day(df: pd.DataFrame, value_col: str) -> pd.DataFrame:
    result = df.copy()
    result[f'{value_col}_rolling_7d'] = result[value_col].rolling(window=7, min_periods=1).mean()
    return result


def cumulative_sum_per_group(df: pd.DataFrame, group_col: str, value_col: str) -> pd.DataFrame:
    result = df.copy()
    result[f'{value_col}_cumsum'] = result.groupby(group_col)[value_col].cumsum()
    return result
