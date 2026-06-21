import pandas as pd
import numpy as np


def calculate_total_spending(df: pd.DataFrame) -> pd.DataFrame:
    """
    Create a new column 'TotalSpending' by summing up:
    'RoomService', 'FoodCourt', 'ShoppingMall', 'Spa', and 'VRDeck'.
    Handle missing values by treating them as 0 before summing.
    Should return the modified DataFrame.
    """
    spending_cols = ["RoomService", "FoodCourt", "ShoppingMall", "Spa", "VRDeck"]
    df["TotalSpending"] = df[spending_cols].fillna(0).sum(axis=1)
    return df


def parse_cabin(df: pd.DataFrame) -> pd.DataFrame:
    """
    The 'Cabin' column is in the format 'Deck/Num/Side' (e.g., 'B/0/P').
    Split this into three new columns: 'Deck', 'CabinNum', and 'Side'.
    If 'Cabin' is NaN, these new columns should also be NaN.
    'CabinNum' should be converted to numeric (float or int).
    Should return the modified DataFrame.
    """
    cabin_parts = df["Cabin"].str.split("/", expand=True)

    df["Deck"] = cabin_parts[0]
    df["CabinNum"] = pd.to_numeric(cabin_parts[1], errors="coerce")
    df["Side"] = cabin_parts[2]

    return df


def filter_outliers_iqr(df: pd.DataFrame, column_name: str) -> pd.DataFrame:
    """
    Identify and remove outliers in the specified column using the IQR method.
    """
    Q1 = df[column_name].quantile(0.25)
    Q3 = df[column_name].quantile(0.75)
    IQR = Q3 - Q1

    lower = Q1 - 1.5 * IQR
    upper = Q3 + 1.5 * IQR

    filtered_df = df[
        (df[column_name] >= lower) &
        (df[column_name] <= upper)
    ]

    return filtered_df


if __name__ == "__main__":
    try:
        print("Assignment 2 template ready for implementation.")
    except Exception as e:
        print(f"Error: {e}")



        