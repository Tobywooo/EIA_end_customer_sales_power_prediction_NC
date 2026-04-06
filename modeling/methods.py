import pandas as pd
import os

def ETL(os_path, csv_filename, stateid, drop_columns, keep_columns):
    full_path = os.path.join(os_path, csv_filename)
    df_raw = pd.read_csv(full_path)

    df_filtered = df_raw[df_raw["stateid"] == stateid]
    df_result = df_filtered.drop(columns=drop_columns, errors="ignore").copy()

    if len(keep_columns) > 1:
        new_col_name = "_".join(keep_columns)
        df_result[new_col_name] = (
            df_result[keep_columns]
            .astype(str)
            .agg("".join, axis=1)
        )
        df_result = df_result.drop(columns=keep_columns, errors="ignore")

    df_result = df_result.drop(columns=["stateDescription"], errors="ignore")

    return df_result