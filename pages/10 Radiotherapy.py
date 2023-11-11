import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
@st.cache_data()
def load_radiotherapy_data():
    df = pd.read_csv('datasets\Radiotherapy equipment.csv')
    return df

st.sidebar.image('images/Radiotherapy.png')
with st.spinner("loading dataset"):
    df = load_radiotherapy_data()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("Radioherapy_equipment.csv datasets"):
    st.subheader('🏥 RADIO THERAPY DATA')
    st.dataframe(df)

#location
st.header('LOCATION Based Visualization')
location_count = df['LOCATION'].value_counts()
fig1 = px.pie(location_count, location_count.index, location_count.values)
st.plotly_chart(fig1, use_container_width=True)

#time
st.header('Time Based Visualization')
time_count = df['TIME'].value_counts()
fig1 = px.bar(time_count, time_count.index, time_count.values)
st.plotly_chart(fig1, use_container_width=True)

#value
st.header('Value Based Visualization')
value_count = df['Value'].value_counts()
fig1 = px.bar(value_count, value_count.index, value_count.values)
st.plotly_chart(fig1, use_container_width=True)

#flag
st.header('Flag Codes Based Visualization')
flag_codes_count = df['Flag Codes'].value_counts()
fig1 = px.pie(flag_codes_count, flag_codes_count.index, flag_codes_count.values)
st.plotly_chart(fig1, use_container_width=True)