"""Solution for Merging"""
import pandas as pd


def merge_with_missing_handling(df1: pd.DataFrame, df2: pd.DataFrame, key: str) -> pd.DataFrame:
    result = df1.merge(df2, on=key, how='left')
    # Fill numeric columns with 0
    numeric_cols = result.select_dtypes(include='number').columns
    result[numeric_cols] = result[numeric_cols].fillna(0)
    return result
