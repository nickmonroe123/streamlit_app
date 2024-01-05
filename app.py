import streamlit as st
import yfinance as yf
from pandas_datareader import data as pdr
import datetime

yf.pdr_override()

# Title of the app
st.title('Stock Historical Data and News')

# Create columns for date input
col1, col2 = st.columns(2)

start_date = col1.date_input('Start date', datetime.date.today() - datetime.timedelta(days=365))
end_date = col2.date_input('End date', datetime.date.today())

ticker = st.text_input('Enter a valid ticker') # User inputs the ticker

if ticker: # If ticker is not an empty string
    with st.spinner('Searching...'): # Display a spinner and a message while loading
        valid_ticker = True
        try:
            data = pdr.get_data_yahoo(ticker, start=start_date, end=end_date)
        except:
            valid_ticker = False

    if valid_ticker: # If ticker is valid
        st.success('Done!')
        st.write(f"Showing data for {ticker}")
        st.line_chart(data['Close']) # Plot the closing prices

        # TODO: Add code to fetch and display news here

    else: # If ticker is invalid
        st.error("Failed to find ticker. Please enter a valid ticker")

else: # If ticker is an empty string
    st.write("Please enter a ticker")