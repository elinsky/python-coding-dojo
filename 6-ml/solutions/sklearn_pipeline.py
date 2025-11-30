"""Solution for M4.01: sklearn Pipeline Builder"""
import numpy as np
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler, OneHotEncoder
from sklearn.impute import SimpleImputer
from sklearn.linear_model import LogisticRegression


def build_preprocessor(
    numeric_cols: list[str],
    categorical_cols: list[str]
) -> ColumnTransformer:
    """Build a ColumnTransformer for preprocessing."""
    transformers = []

    if numeric_cols:
        numeric_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='mean')),
            ('scaler', StandardScaler())
        ])
        transformers.append(('num', numeric_transformer, numeric_cols))

    if categorical_cols:
        categorical_transformer = Pipeline(steps=[
            ('imputer', SimpleImputer(strategy='most_frequent')),
            ('onehot', OneHotEncoder(handle_unknown='ignore'))
        ])
        transformers.append(('cat', categorical_transformer, categorical_cols))

    return ColumnTransformer(transformers=transformers)


def build_pipeline(
    preprocessor: ColumnTransformer,
    model
) -> Pipeline:
    """Build a complete pipeline."""
    return Pipeline(steps=[
        ('preprocessor', preprocessor),
        ('classifier', model)
    ])


def fit_and_evaluate(
    pipeline: Pipeline,
    X_train: pd.DataFrame,
    y_train: np.ndarray,
    X_test: pd.DataFrame,
    y_test: np.ndarray
) -> float:
    """Fit pipeline and return test accuracy."""
    pipeline.fit(X_train, y_train)
    return pipeline.score(X_test, y_test)


if __name__ == '__main__':
    import sys
    from pathlib import Path
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
