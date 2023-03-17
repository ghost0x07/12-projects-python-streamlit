import streamlit as st
import yfinance as yf

st.write("""
# Simple Stock Price App

Displays closing price and volume for Google (ticker: `GOOG`) :sunglasses:
""")

ticker = "GOOG"
data = yf.download(ticker, period="1d", start="2010-5-31", end="2020-5-31")

st.write("# Historical Data")
st.write(data)

st.write("# Closing Price")
st.line_chart(data.Close)
st.write("# Volume")
st.line_chart(data.Volume)
