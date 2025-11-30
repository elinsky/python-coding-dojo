"""Solution for Filtering"""
import pandas as pd


def filter_by_conditions(df: pd.DataFrame) -> pd.DataFrame:
    return df[(df['age'] > 30) & (df['city'] == 'Chicago')]


def unique_value_counts(df: pd.DataFrame, column: str) -> pd.Series:
    return df[column].value_counts()
