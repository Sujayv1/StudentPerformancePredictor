import pandas as pd


def load_data(filepath):
    df = pd.read_csv(filepath)

    print("\nDataset Preview:")
    print(df.head())

    print("\nDataset Info:")
    print(df.info())

    print("\nMissing Values:")
    print(df.isnull().sum())

    return df