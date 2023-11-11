import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
def load_MRIunits_data():
    df = pd.read_csv('datasets\Magnetic resonance imaging (MRI) units.csv')
    return df

st.sidebar.image('images\MRI units.png')
with st.spinner("loading dataset"):
    df = load_MRIunits_data()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("MRI units.csv datasets"):
    st.subheader('🥼 MRI UNITS DATA')
    st.dataframe(df)

#location
st.header('Loaction Based  visualization')
location_count = df['LOCATION'].value_counts()
fig1 = px.area(location_count, location_count.index,location_count.values)
st.plotly_chart(fig1, use_container_width=True)

#subject
st.header('Subject Based Visualization')
subject_count = df['SUBJECT'].value_counts()
fig1 = px.pie(subject_count, subject_count.index,subject_count.values)
st.plotly_chart(fig1, use_container_width=True)

#value
st.header('Value Based Visualization')
value_count = df['Value'].value_counts()
fig1 = px.bar(value_count, value_count.index,value_count.values)
st.plotly_chart(fig1, use_container_width=True)

#time
st.header('Time Based Visualization')
time_count = df['TIME'].value_counts()
fig1 = px.line(time_count, time_count.index,time_count.values)
st.plotly_chart(fig1, use_container_width=True)