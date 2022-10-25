import re
import pandas as pd

def cleaning_df (path):
    df = pd.read_csv(path, index_col = 0, encoding = 'unicode_escape')
    df["charname"] = df.charname.apply(lambda x: x.replace(" ", ""))
    df["birthname"] = df.birthname.apply(lambda x: x.replace(" ", ""))
    df.to_csv("Datasource\clean.csv")
    print("Dataframe has been cleaned")
    return df