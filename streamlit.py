import pandas as pd
import streamlit as st

videoGame_df = pd.read_csv('data/vgSales.csv')
happiness_df = pd.read_csv('data/happinessReport.csv')

st.header('Video Game Sales Data & Trending YouTube Statistics')

# checkbox to see dataframes
if st.checkbox('Video Game Sales Data'):
    st.dataframe(videoGame_df)
if st.checkbox('Happiness Report'):
    st.dataframe(happiness_df)


# creating charts for data visualization
st.subheader('Video Game Sales by Genre')
vgGenre = videoGame_df['Genre'].value_counts()
st.bar_chart(vgGenre)
st.caption('Displays a bar chart of number genre during sales')

st.subheader('Happiness Report by Score')
happinessScore = happiness_df['score']
st.line_chart(happinessScore)
st.caption('Displays a line chart of scores countries')

code = '''Code behind the first chart for Video Game Sales
happinessScore = happiness_df['score']
st.line_chart(happinessScore)
'''
st.code(code, language='python')
