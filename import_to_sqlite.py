import pandas as pd
import sqlite3
import numpy as np

# File paths
plays_csv = 'packers_plays.csv'
roster_csv = 'packers_roster.csv'
db_path = 'packers.db'

def infer_sqlite_types(df):
    types = {}
    for col in df.columns:
        dtype = df[col].dtype
        # Handle pandas nullable dtypes
        if str(dtype) in ['Int64', 'int64', 'UInt8', 'UInt16', 'UInt32', 'UInt64']:
            types[col] = 'INTEGER'
        elif str(dtype) in ['Float64', 'float64']:
            types[col] = 'REAL'
        else:
            types[col] = 'TEXT'
    return types

def import_csv_to_sqlite(csv_path, table_name, conn):
    df = pd.read_csv(csv_path)
    # Convert columns to best types
    df = df.convert_dtypes()
    types = infer_sqlite_types(df)
    # Create table
    columns = ', '.join([f'"{col}" {types[col]}' for col in df.columns])
    conn.execute(f'CREATE TABLE IF NOT EXISTS {table_name} ({columns});')
    # Insert data
    df.to_sql(table_name, conn, if_exists='replace', index=False)

if __name__ == '__main__':
    conn = sqlite3.connect(db_path)
    import_csv_to_sqlite(plays_csv, 'packers_plays', conn)
    import_csv_to_sqlite(roster_csv, 'packers_roster', conn)
    conn.close()
    print(f"Database '{db_path}' created with tables 'packers_plays' and 'packers_roster'.")
