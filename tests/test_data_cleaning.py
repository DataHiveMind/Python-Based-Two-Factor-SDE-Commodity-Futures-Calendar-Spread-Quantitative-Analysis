"""
tests/test_data_cleaning.py
Purpose: This module contains tests for the data cleaning functions in the `clean_missing_values` module.
Aims:
    1. Test the identification of missing values in a DataFrame.
    2. Test the handling of missing values using different strategies.
    3. Test the summarization of missing values before and after cleaning.
"""

import pandas as pd
from src.data_cleaning.clean_missing_values import identify_missing_values, handle_missing_values, summarize_missing_values
import pytest

@pytest.fixture
def sample_data():
    """
    Fixture to create a sample DataFrame with missing values for testing.
    
    Returns:
        pd.DataFrame: A sample DataFrame with some missing values.
    """
    data = {
        'A': [1, 2, None, 4],
        'B': [None, 5, 6, 7],
        'C': [8, None, None, 10]
    }
    return pd.DataFrame(data)

def test_identify_missing_values(sample_data):
    """
    Test the identify_missing_values function.
    
    Args:
        sample_data (pd.DataFrame): The sample DataFrame with missing values.
    """
    missing_counts = identify_missing_values(sample_data)
    expected_counts = pd.Series({'A': 1, 'B': 1, 'C': 2})
    pd.testing.assert_series_equal(missing_counts, expected_counts)

def test_handle_missing_values_drop(sample_data):
    """
    Test the handle_missing_values function with 'drop' strategy.

    Args:
        sample_data (pd.DataFrame): The sample DataFrame with missing values.
    """
    cleaned_data = handle_missing_values(sample_data, strategy='drop')
    expected_data = sample_data.dropna()
    pd.testing.assert_frame_equal(cleaned_data, expected_data)

def test_handle_missing_values_impute(sample_data):
    """
    Test the handle_missing_values function with 'impute' strategy.

    Args:
        sample_data (pd.DataFrame): The sample DataFrame with missing values.
    """
    cleaned_data = handle_missing_values(sample_data, strategy='impute')
    expected_data = sample_data.fillna(sample_data.mean())
    pd.testing.assert_frame_equal(cleaned_data, expected_data)

def test_handle_missing_values_invalid_strategy(sample_data):
    """
    Test the handle_missing_values function with an invalid strategy.

    Args:
        sample_data (pd.DataFrame): The sample DataFrame with missing values.
    """
    with pytest.raises(ValueError, match="Invalid strategy. Choose 'drop' or 'impute'."):
        handle_missing_values(sample_data, strategy='invalid')
    
def test_summarize_missing_values(sample_data):
    """
    Test the summarize_missing_values function.

    Args:
        sample_data (pd.DataFrame): The sample DataFrame with missing values.
    """
    before_cleaning = identify_missing_values(sample_data)
    cleaned_data = handle_missing_values(sample_data, strategy='impute')
    after_cleaning = identify_missing_values(cleaned_data)
    summary = summarize_missing_values(sample_data, before_cleaning, after_cleaning)
    
    expected_summary = pd.DataFrame({
        'Before Cleaning': before_cleaning,
        'After Cleaning': after_cleaning
    })
    pd.testing.assert_frame_equal(summary, expected_summary)

    assert summary['Before Cleaning'].sum() > summary['After Cleaning'].sum()

