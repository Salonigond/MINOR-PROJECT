import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
@st.cache_data()
def load_vaccination_data():
    df = pd.read_csv(r'datasets\Child vaccination rates.csv')
    return df

st.sidebar.image('images\Child.png')
with st.spinner("loading dataset"):
    df = load_vaccination_data()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("Show vaccination dataset"):
    st.subheader('💉 CHILD VACCINATION DATA')
    st.dataframe(df)

#Subject
st.header('Subject based visualization')
subject_count = df['SUBJECT'].value_counts()
fig1 = px.pie(subject_count, subject_count.index, subject_count.values)
st.dataframe(subject_count, use_container_width=True)
st.plotly_chart(fig1, use_container_width=True)

#time
st.header('Time based Visualization')
time_count = df['TIME'].value_counts()
fig1 = px.bar(time_count, time_count.index, time_count.values)
st.plotly_chart(fig1, use_container_width=True)

#location
st.header('Loaction Based Visualization')
location_count = df['LOCATION'].value_counts()
fig1 = px.area(location_count, location_count.index,location_count.values)
st.plotly_chart(fig1, use_container_width=True)

#value
st.header('Value Based Visulization')
value_count= df['Value'].value_counts()
fig1 = px.bar(value_count, value_count.index,value_count.values)
st.plotly_chart(fig1, use_container_width=True)
