import streamlit as st
import yfinance as yf
df_test = yf.download("BTC-USD", period="1mo", interval="1d")
st.write(df_test)
