# load_data.py
import pandas as pd

def load_data(path):
    df = pd.read_csv(path)
    df['Cals_per100grams'] = df['Cals_per100grams'].str.replace(' cal', '', regex=False).astype(int)
    df['KJ_per100grams'] = df['KJ_per100grams'].str.replace(' kJ', '', regex=False).astype(int)
    return df
