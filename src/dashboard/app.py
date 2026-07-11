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

first_value = df_filter["Close"].iloc[0]
last_value = df_filter["Close"].iloc[-1]

total_r = (last_value - first_value) / first_value * 100

max_volatility = df_filter["Close"].max()
min_volatility = df_filter["Close"].min()
mean = df_filter["Volatility"].mean()

st.title("Period Metrics ")

col1, col2, col3, col4 = st.columns(4)

with col1:
    st.metric(
        label="Average Volatility", 
        value=f"{mean:.2%} "
    )

with col2:
    st.metric(
        label="Max Price ", 
        value=f" $ {max_volatility:,.2f} ",
        delta=None
    )

with col3:
    st.metric(
        label="Minimal Price ", 
        value=f" $ {min_volatility:,.2f} "
    )

with col4:
    st.metric(
        label="Total Return ", 
        value=f"{total_r:.2f} %"
    )


st.dataframe(df_filter, width='stretch', hide_index=True) 