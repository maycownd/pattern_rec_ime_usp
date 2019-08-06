import pandas as pd
from sklearn.preprocessing import MinMaxScaler


def split_text(df: pd.DataFrame, column: object) -> list:
    return [i[1:-1] for i in df[column].str.split("")]


def transform_data(df, column='octamer'):
    return df[column].apply(lambda x: [i for i in x])


def scale_data(x, scaler=None):
    if not scaler:
        scaler = MinMaxScaler(feature_range=(-1, 1))
        scaler.fit(x)
    x = scaler.transform(x)
    return x, scaler
