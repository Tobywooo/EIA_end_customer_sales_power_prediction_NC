import pandas as pd
import os

def ETL(os_path, csv_filename, stateid, drop_columns, keep_columns):       
    #This method will take the raw data from your original data retrieval file and creates your specific modeling dataset
    #This method only adds together 2 columns. Modify it if you need more
    full_path = os.path.join(os_path, csv_filename)
    df_raw = pd.read_csv(full_path)
    df_raw = df_raw[df_raw['stateid'] == stateid]
    df_dropped = df_raw.drop(columns=drop_columns)
    df_combined = df_dropped.copy()
    df_combined[keep_columns[0] + '_' + keep_columns[1]] = df_dropped[keep_columns[0]] + df_dropped[keep_columns[1]]
    df_combined = df_combined.drop(columns=[keep_columns[0], keep_columns[1], "stateDescription"])
    return df_combined