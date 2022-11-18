import pandas as pd
import streamlit as st

riot_data = 'data/LoL_Champion_Data.csv'
twitter_data = 'data/twitter_stocks.csv'

def get_data(data):
    return pd.read_csv(data)

# reading dataset
league_df = get_data(riot_data)
twitter_df = get_data(twitter_data)

# creating dashboard title
st.header('League of Legends & Twitter Stocks Data')

# adding dashboard caption
st.caption('History of League of Legends & Twitter Stocks Data')

# displaying each dataframe
if st.checkbox('League of Legends Data'):
    st.dataframe(league_df)

if st.checkbox('Twitter Stock'):
    st.dataframe(twitter_data)
