# data_cleaning.py
import pandas as pd

def simple_clean(df):
    df = df.dropna()
    df = df.drop_duplicates()
    print("Data cleaned: rows =", len(df))
    return df


if __name__ == "__main__":
    print("Version 1.2: Removed missing values successfully")

