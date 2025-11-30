#!/usr/bin/env python3
"""M4.01: sklearn Pipeline Builder

Build a preprocessing and modeling pipeline using sklearn.

Problem:
    Create a pipeline that:
    1. Handles missing values (imputation)
    2. Scales numeric features
    3. Encodes categorical features
    4. Trains a model

    Use ColumnTransformer for different feature types.

Functions to implement:
    1. build_preprocessor(numeric_cols, categorical_cols) -> ColumnTransformer
       - StandardScaler for numeric
       - OneHotEncoder for categorical
       - SimpleImputer for missing values

    2. build_pipeline(preprocessor, model) -> Pipeline
       - Chain preprocessor and model

    3. fit_and_evaluate(pipeline, X_train, y_train, X_test, y_test) -> accuracy

Example:
    numeric_cols = ['age', 'income']
    categorical_cols = ['gender', 'city']

    preprocessor = build_preprocessor(numeric_cols, categorical_cols)
    pipeline = build_pipeline(preprocessor, LogisticRegression())
    accuracy = fit_and_evaluate(pipeline, X_train, y_train, X_test, y_test)

Edge Cases:
    - All numeric or all categorical
    - Unknown categories at test time
    - All missing values in a column

Complexity:
    Time: O(n * d) for preprocessing
    Space: O(n * d_encoded) for one-hot encoding
"""

import numpy as np
import pandas as pd
from pathlib import Path
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression


def build_preprocessor(
    numeric_cols: list[str],
    categorical_cols: list[str]
) -> ColumnTransformer:
    """Build a ColumnTransformer for preprocessing.

    Args:
        numeric_cols: List of numeric column names
        categorical_cols: List of categorical column names

    Returns:
        ColumnTransformer with appropriate transformers
    """
    # TODO - you fill in here.
    return ColumnTransformer(transformers=[])


def build_pipeline(
    preprocessor: ColumnTransformer,
    model
) -> Pipeline:
    """Build a complete pipeline.

    Args:
        preprocessor: ColumnTransformer for preprocessing
        model: sklearn estimator

    Returns:
        Complete Pipeline
    """
    # TODO - you fill in here.
    return Pipeline(steps=[])


def fit_and_evaluate(
    pipeline: Pipeline,
    X_train: pd.DataFrame,
    y_train: np.ndarray,
    X_test: pd.DataFrame,
    y_test: np.ndarray
) -> float:
    """Fit pipeline and return test accuracy.

    Args:
        pipeline: sklearn Pipeline
        X_train, y_train: Training data
        X_test, y_test: Test data

    Returns:
        Accuracy score on test set
    """
    # TODO - you fill in here.
    return 0.0


if __name__ == '__main__':
    import sys
    sys.path.insert(0, str(Path(__file__).parent.parent))
    from test_framework import run_tests

    def test_wrapper(train_data, test_data, numeric_cols, categorical_cols):
        X_train = pd.DataFrame(train_data['X'])
        y_train = np.array(train_data['y'])
        X_test = pd.DataFrame(test_data['X'])
        y_test = np.array(test_data['y'])

        preprocessor = build_preprocessor(numeric_cols, categorical_cols)
        pipeline = build_pipeline(preprocessor, LogisticRegression())
        accuracy = fit_and_evaluate(pipeline, X_train, y_train, X_test, y_test)
        return round(accuracy, 4)

    exit(run_tests('sklearn_pipeline_tests.json', test_wrapper))
