import pandas as pd
import streamlit as st
import yfinance as yf
import datetime

st.write(
    """
    # Stock Price Analyser
    Shown are the stock prices of Apple."""
)  

ticker_symbol=st.text_input(
            'Enter stock symbol',
            'AAPL',
            key='placeholder'
)

col1,col2= st.columns(2)
## start date analysis
with col1:
    start= st.date_input("INPUT STARTING DATE",
              datetime.date(2018,1,1))

with col2:
    end= st.date_input("INPUT END DATE",
                   datetime.date(2020,12,31))


ticker_data= yf.Ticker(ticker_symbol)
data=ticker_data.history(period='1d',start=f'{start}', end=f'{end}')
st.write(
    f"""
    ### {ticker_symbol}'s EOD data
    """
)
st.dataframe(data)

st.write("""
## Daily closing price chart""")
st.line_chart(data.Close)

st.write("""
## Volume of shares traded each day""")
st.line_chart(data.Volume)


