import sqlite3

def load(df):
    conn = sqlite3.connect("database/data.db")
    df.to_sql("data_table", conn, if_exists="replace", index=False)
    conn.close()
