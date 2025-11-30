"""Solution for DataFrame Creation"""
import pandas as pd


def create_df_from_dict() -> pd.DataFrame:
    return pd.DataFrame({
        'name': ["Alice", "Bob", "Charlie"],
        'age': [25, 30, 35],
        'city': ["NYC", "LA", "Chicago"]
    })


def explore_dataframe(df: pd.DataFrame) -> dict:
    return {
        'head': df.head(),
        'dtypes': df.dtypes,
        'missing_counts': df.isna().sum()
    }
