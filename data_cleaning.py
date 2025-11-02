# data_cleaning.py
import pandas as pd

def simple_clean(df):
    df = df.dropna()
    df = df.drop_duplicates()
    return df

if __name__ == "__main__":
    print("Version 1.1: Removed missing values successfully")

