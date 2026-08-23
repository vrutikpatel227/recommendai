import pandas as pd

def preprocess(df: pd.DataFrame) -> pd.DataFrame:
    """
    Clean dataset: remove duplicates, handle missing values.
    """
    df = df.drop_duplicates()
    df = df.fillna("")
    return df
