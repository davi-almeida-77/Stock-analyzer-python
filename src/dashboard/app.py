import streamlit as st
import pandas as pd
from pathlib import Path

st.title("Market Stock Analyzer")

file_path = Path(__file__).resolve().parents[2] / "data" / "processed" / "stocks_processed.xlsx"


df = pd.read_excel( file_path )

st.dataframe(df, use_container_width=True, hide_index=True)