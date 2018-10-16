import pandas as pd
import copy 
def get_df_from_file(filename):
    return pd.read_csv(filename, low_memory=False)

def get_message_type_from_raw_df(raw_df):
    return raw_df.iloc[:, 0]

def get_message_type_count(raw_df):
    message_type = get_message_type_from_raw_df(raw_df)
    return raw_df.groupby([message_type]).apply(len)

def get_unique_message_types(raw_df): 
    return raw_df.iloc[:, 0].unique()

def create_indexed_frames_by_message(raw_df): 
    unique_message_types = get_unique_message_types(raw_df)
    message_dfs = {}
    for message_type in unique_message_types: 
        message_dfs[message_type] = raw_df[raw_df.iloc[:, 0]== message_type] 
    return message_dfs
