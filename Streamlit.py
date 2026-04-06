import streamlit as st
import sqlite3
import pandas as pd

conn = sqlite3.connect("database/data.db")
df = pd.read_sql("SELECT * FROM data_table", conn)

st.title("Data Dashboard")
st.dataframe(df)

streamlit run app.py
