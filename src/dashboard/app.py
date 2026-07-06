import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Market Stock Analyzer")

file_path = Path(__file__).resolve().parents[2] / "data" / "processed" / "stocks_processed.xlsx"


df = pd.read_excel( file_path, index_col=None )

df["Date"] = pd.to_datetime(df["Date"]).dt.date

columns = df["Ticker"].unique()

options =  st.selectbox("Chose an Option", columns)

df_filter = df[df["Ticker"] == options]

st.write(f"Data Of {options}:")
st.line_chart(df_filter.set_index("Date")["Close"])


st.dataframe(df_filter, width='stretch', hide_index=True)