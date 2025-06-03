import pandas as pd

def clean_budget_data(path):
    df = pd.read_excel(path)
    df.columns = df.columns.str.strip().str.lower().str.replace(" ", "_")
    df.dropna(how="all", inplace=True)
    return df
