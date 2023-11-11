import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
@st.cache_data()
def load_hospitalbeds_data():
    df = pd.read_csv('datasets\Hospital beds.csv')
    return df

st.sidebar.image('images\Hospital beds.png')
with st.spinner("loading dataset"):
    df = load_hospitalbeds_data()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("Hospital Beds.csv datasets"):
    st.subheader('🛏️ HOSPITAL BEDS DATA')
    st.dataframe(df)
   
#time
st.header('Time Based Visualization')
time_count = df['TIME'].value_counts()
fig1 = px.area(time_count, time_count.index,time_count.values)
st.plotly_chart(fig1, use_container_width=True)

#value
st.header('Value Based Visulization')
value_count= df['Value'].value_counts()
fig1 = px.bar(value_count, value_count.index,value_count.values)
st.plotly_chart(fig1, use_container_width=True)

#flag
st.header('Flag Based Visualization')
flag_count = df['Flag Codes'].value_counts()
fig1 = px.pie(flag_count, flag_count.index,flag_count.values)
st.plotly_chart(fig1, use_container_width=True)

#location
st.header('Loaction Based Visualization')
location_count = df['LOCATION'].value_counts()
fig1 = px.area(location_count, location_count.index,location_count.values)
st.plotly_chart(fig1, use_container_width=True)
