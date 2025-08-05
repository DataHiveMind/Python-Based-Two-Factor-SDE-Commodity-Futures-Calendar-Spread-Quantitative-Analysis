"""
src/data_cleaning/clean_missing_values.py

Purpose: This module contains functions to clean missing values in datasets. 

Aims:
    1. Identify missing values in the dataset.
    2. Handle missing values by either removing or imputing them.
    3. Provide a summary of the missing values before and after cleaning.
    4. Ensure the dataset is ready for further analysis or modeling.

"""
import pandas as pd

def identify_missing_values(df: pd.DataFrame) -> pd.Series:
    """
    Identify missing values in the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
    
    Returns:
        pd.Series: A Series containing the count of missing values for each column.
    """
    return df.isnull().sum()

def handle_missing_values(df: pd.DataFrame, strategy: str = 'drop') -> pd.DataFrame:
    """
    Handle missing values in the DataFrame.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        strategy (str): The strategy to handle missing values. Options are 'drop' and 'impute'.
    
    Returns:
        pd.DataFrame: The DataFrame after handling missing values.
    """
    if strategy == 'drop':
        return df.dropna()
    elif strategy == 'impute':
        return df.fillna(df.mean())
    else:
        raise ValueError("Invalid strategy. Choose 'drop' or 'impute'.")

def summarize_missing_values(df: pd.DataFrame, before_cleaning: pd.Series, after_cleaning: pd.Series) -> pd.DataFrame:
    """
    Summarize the missing values before and after cleaning.
    
    Args:
        df (pd.DataFrame): The input DataFrame.
        before_cleaning (pd.Series): Missing values count before cleaning.
        after_cleaning (pd.Series): Missing values count after cleaning.
    
    Returns:
        pd.DataFrame: A DataFrame summarizing the missing values.
    """
    summary = pd.DataFrame({
        'Before Cleaning': before_cleaning,
        'After Cleaning': after_cleaning
    })
    return summary

#------------------------------------------------------------------
# Example usage
#------------------------------------------------------------------

if __name__ == "__main__":
    # Load a sample DataFrame
    data = {
        'A': [1, 2, None, 4],
        'B': [None, 2, 3, 4],
        'C': [1, None, None, 4]
    }
    df = pd.DataFrame(data)

    # Identify missing values
    missing_before = identify_missing_values(df)
    
    # Handle missing values
    cleaned_df = handle_missing_values(df, strategy='impute')
    
    # Identify missing values after cleaning
    missing_after = identify_missing_values(cleaned_df)
    
    # Summarize missing values
    summary = summarize_missing_values(df, missing_before, missing_after)
    
    print(summary)
    # Output the summary of missing values
    print("Cleaned DataFrame:")
    print(cleaned_df)