import datetime
import time

import pandas as pd
import langdetect

def clean_missing_data(df):
    print(df.isna().sum())

    df = df.dropna()
    df = df[df["contents"] != " "]
    df = df.reset_index(drop=True)
    return df

def keep_english(df):
    # Extrait de la documentation https://pypi.org/project/langdetect/#description
    # langdetect Language detection algorithm is non-deterministic,
    # which means that if you try to run it on a text which is either too short or too ambiguous,
    # you might get different results everytime you run it.
    # To enforce consistent results, call following code before the first language detection:
    langdetect.DetectorFactory.seed = 0

    start = time.time()
    n = len(df)
    df['language'] = df['contents'].apply(lambda x: langdetect.detect(x[:2000]))

    EN = (df['language'] == 'en').sum()
    OTHERS = n - EN

    print("Proportion de discours en anglais : ", EN / n)
    end = time.time()

    print("Temps pris par cette méthode : ", end - start)

    # On retire les discours qui ne sont pas en anglais des données à analyser
    df = df[df['language'] == 'en'].reset_index(drop=True)

    return df

def add_date(df):
    df["Year"] = df.date.str[:4].astype(int)
    df["Month"] = df.date.str[5:7].astype(int)
    df["Day"] = df.date.str[8:].astype(int)

    week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
    months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October',
              'November', 'December']
    df["DayofWeek"] = pd.Series(dtype=int)
    df["DayofWeek_str"] = pd.Series(dtype=str)
    df["Month_str"] = pd.Series(dtype=str)
    for i in range(len(df)):
        df["DayofWeek"][i] = int(datetime.date(df["Year"][i], df["Month"][i], df["Day"][i]).isoweekday())
        df["DayofWeek_str"][i] = week[int(datetime.date(df["Year"][i], df["Month"][i], df["Day"][i]).weekday())]
        df["Month_str"][i] = months[df["Month"][i] - 1]

    # .weekday() : from 0 to 6
    # .isoweekday() : from 1 to 7

    df["DayofWeek"] = df["DayofWeek"].astype(int)
    return df

def todisk(df, path = r"data\clean_ecb_speeches_dataset.csv"):
    df.to_csv(path_or_buf=path,
              sep=',',
              header=True,
              index=False,
              encoding='utf-8'
              )
    return None

def fromdisk(path = r"data\clean_ecb_speeches_dataset.csv"):
    return pd.read_csv(path)