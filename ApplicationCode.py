import streamlit as st
import pandas as pd
from ForbesFedRatesHike import RatesDates  # Assuming this fetches Fed Rate hike data
from RedditApi import df_concat
from NewYahooApi import fetchyahooresults
import matplotlib.pyplot as plt

df = df_concat

# Title and header
st.title('Stock Sentiment Analysis App')

# Author information
st.sidebar.markdown("**Author:** Tushar Elangovan")

# Web Appの説明 (Explanation)
st.markdown("""
## How to Use the App

The side bar on the left side gives us the options for 2 filters. 
            
**Interactive Features:**

* Filter data by Fed Rate Hike Dates and Stock Ticker symbol in the sidebar.
* Click "Fetch Yahoo Results" to retrieve the historical data for that particular stock. (Note: Currently, available data may be limited & some stocks might not have the data)
* View a graph of the opening and closing prices for the fetched data. -> This can be used to verify the reddit sentiment v/s the actual stock price performance

**Content Explanation:**

* After selecting the fed dates and the ticker we can observe the reddit sentiment and the actual stock performance. This gives us an understanding of how well reddit comments are in predicting the stock market prices.
            
**Conclusions:**

* After analyzing the stocks we are able to come to a conclusion that the reddit comments were able to accuratley predict approximatley 50% of the stock performance.

**Gotchas:**

* The current yahoo website doesnt contain historical data for all the stocks and as a result we will not be able to predict the accuracy for the entire dataset.
* Future improvements include adding more data sources, analysis features & better website which contains all stocks historical information for free.
""")

# Create sidebar for filters
with st.sidebar:
    st.subheader('Filters')
    name_options = df['Date'].unique()
    selected_name = st.selectbox('Choose the Fed Hike Date:', name_options)

    # Include "All" option in ticker dropdown
    ticker_options = ['All'] + (df[df['Date'] == selected_name]['ticker'].tolist() if selected_name else [])
    selected_ticker = st.selectbox('Select a ticker to filter:', ticker_options, key='ticker')

    # Fetch button below the ticker filter
    fetch_button = st.button('Fetch Yahoo Results')

# Filter DataFrame based on selections (name and ticker)
filtered_df = df.copy()  # Avoid modifying original DataFrame
if selected_name:
    filtered_df = filtered_df[filtered_df['Date'] == selected_name]
if selected_ticker != 'All':  # Filter only if "All" is not selected
    filtered_df = filtered_df[filtered_df['ticker'] == selected_ticker]

# Display the filtered DataFrame (excluding the name column)
st.subheader('Filtered Stock Data')
st.dataframe(filtered_df.iloc[:, 1:])  # Select all columns except 'name'

# Fetch data and display results only when button is pressed
if fetch_button and selected_ticker != 'All':
    try:
        fetched_data = fetchyahooresults(selected_ticker, selected_name)
        st.subheader('Fetched Yahoo Results')
        st.write(fetched_data)

        opening_price = fetched_data["Opening Price"]
        closing_price = fetched_data["Closing Price"]
        categories = ['Open', 'Close']
        
        # Create the graph
        print('2 good')
        x_values = [0,1]

        plt.figure()
        plt.plot([opening_price, closing_price], marker="o", label=categories)  # Use labels as legend entries
        plt.xticks(range(len(categories)), categories)   # Set custom x-axis labels
        plt.xlabel("Time")
        plt.ylabel("$ Stock Price")
        plt.title("Stock Price at Start and End of Trading")
        plt.legend()
        st.pyplot(plt.gcf())


    except:
        fetched_data = "Unfortunately Historical Data Not Available for this Stock, Please Try another Stock"
        st.write(fetched_data)

# Project Description
st.markdown("""
## Project Description

**What did you set out to study?**
            
* I wanted to understand how well reddit comments can predict the stock prices and hence, I strategically chose the Fed Rate Hike dates as those are the dates with the most stock market activity.
            
**Discovery & Conclusions**
            
* The reddit comments have around 50% accuracy in predicting the stock performance. My original hypothesis was that the stocks could predict approximately lower than 50% of the stock prices accurately.
            
**Difficulties**
            
* Creating a consolidated database after scraping data from two sources was definitely the most challenging part of this project. 
            
**Skills**

* User interface design skills would be definitely beneficial in creating this project as the website would be more appealing to interact with and look at. 
            
**Next Steps**
            
* Expand Data Sources: Integrate additional data sources beyond Yahoo Finance. This could include alternative stock market APIs, financial news aggregators, or social media sentiment analysis tools.
            
* Predictive Analysis: Explore the possibility of integrating machine learning models to predict future stock prices based on historical data and news sentiment analysis.
    
* Comparative Analysis: Allow users to compare the performance and sentiment of multiple stocks side-by-side.

""")