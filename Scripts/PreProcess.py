import pandas as pd
import numpy as np

def get_cols_with_no_nans(df):
    cols_with_no_nans = []
    for col in df.columns:
        if df[col].isnull().sum() > 100:
            cols_with_no_nans.append(col)
    return cols_with_no_nans

def ToFullMatrix(path):
    csv_data = pd.read_csv(path,encoding='gb18030')#防止弹出警告
    list_data = pd.DataFrame(csv_data)
    num_cols = get_cols_with_no_nans(list_data)
    cut_data = list_data.drop(num_cols, axis = 1)
    add_data = cut_data.fillna(cut_data.mean())
    str_data=ToStr(add_data)
    return str_data

def ToStr(Arr):
    Str_List = Arr.values.tolist()
    for i in Str_List:
        del (i[0])
    for i in range(len(Str_List)):
        for j in range(len(Str_List[i])):
            Str_List[i][j] = str(Str_List[i][j])
    return Str_List