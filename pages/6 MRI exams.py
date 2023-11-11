import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
@st.cache_data()
def load_MRIunits_data():
    df = pd.read_csv('datasets\Magnetic resonance imaging (MRI) exams.csv')
    return df

st.sidebar.image('images\MRI exam.png')
with st.spinner("loading dataset"):
    df = load_MRIunits_data()
    st.sidebar.header("Navigation")

if st.sidebar.checkbox("MRI exams.csv datasets"):
    st.subheader('👩‍⚕️ MRI EXAMS DATA')
    st.dataframe(df)

#loaction
st.header('Location Based Visualization')   
location_count = df['LOCATION'].value_counts()
fig1 = px.bar(location_count, location_count.index,location_count.values,title="location")
st.plotly_chart(fig1, use_cotainer_width=True)

#subject
st.header('Subject Based Visualization')
subject_count = df['SUBJECT'].value_counts()
fig1 = px.bar(subject_count, subject_count.index,subject_count.values)
st.plotly_chart(fig1, use_cotainer_width=True)

#time
st.header('Time Based Visualization')
time_count = df['TIME'].value_counts()
fig1 = px.bar(time_count, time_count.index,time_count.values)
st.plotly_chart(fig1, use_cotainer_width=True)

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
