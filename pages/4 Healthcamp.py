import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
def load_dailysmoker_data():
    df = pd.read_csv('datasets\Health_camp_detail.csv')
    return df

st.sidebar.image('images\Health.png')
with st.spinner("loading dataset"):
    df = load_dailysmoker_data()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("Health_Camp_Detail.csv datasets"):
    st.subheader('🩺HEALTH_CAMP DATA')
    st.dataframe(df)

#catergory
st.header('Healthcamp Category Distribution')
cat1_count = df['Category1'].value_counts()
fig1 = px.pie(cat1_count, cat1_count.index, cat1_count.values)
st.plotly_chart(fig1, use_container_width=True)

#camp start date
st.header('Camp Start Date Visualization')
df['Camp_Start_Date'] = pd.to_datetime(df['Camp_Start_Date'])
datewise = df.set_index('Camp_Start_Date').resample('M').count()
fig2 = px.bar(datewise, datewise.index, 'Category1')
st.plotly_chart(fig2, use_container_width=True)

#camp end date
st.header('Camp End Date Visualization')
df['Camp_End_Date'] = pd.to_datetime(df['Camp_End_Date'])
datewise = df.set_index('Camp_End_Date').resample('M').count()
fig2 = px.bar(datewise, datewise.index, 'Category1')
st.plotly_chart(fig2, use_container_width=True)