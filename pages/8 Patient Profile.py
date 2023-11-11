import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as pc
st.set_page_config(layout='wide')

# function to load the data only once
@st.cache_data()
def load_patientprofile_data():
    df = pd.read_csv('datasets\Patient_Profile.csv',nrows=1000)
    return df

st.sidebar.image('images\Patient profile.png')
with st.spinner("loading dataset"):
    df = load_patientprofile_data()

st.sidebar.header("Navigation")

if st.sidebar.checkbox("Patient Profile.csv datasets"):
    st.subheader('👩🏻‍🤝‍👨🏼PATIENT PROFILE DATA')
    st.dataframe(df)

#patient id
st.header('Patient_ID Based Visualization')
patient_count = df['Patient_ID'].value_counts()
fig1 = px.line(patient_count, patient_count.index,patient_count.values)
st.plotly_chart(fig1, use_container_width=True)

#educarion
st.header('Education Score Based Visualization')
education_score_count = df['Education_Score'].value_counts()
fig1 = px.bar(education_score_count, education_score_count.index,education_score_count.values)
st.plotly_chart(fig1, use_container_width=True)

#age
st.header('Age Based Visualization')
age_count = df['Age'].value_counts()
fig1 = px.bar(age_count, age_count.index, age_count.values)
st.plotly_chart(fig1, use_container_width=True)

#first
st.header('First_Interaction Based Visualization')
first_interaction_count = df['First_Interaction'].value_counts()
fig1 = px.bar(first_interaction_count, first_interaction_count.index,first_interaction_count.values)
st.plotly_chart(fig1, use_container_width=True)

#city type
st.header('City_Type Based Visualization')
city_type_count = df['City_Type'].value_counts()
fig1 = px.pie(city_type_count, city_type_count.index,city_type_count.values)
st.plotly_chart(fig1, use_container_width=True)

#employer
st.header('Employer_Category Based Visualization')
employer_category_count = df['Employer_Category'].value_counts()
fig1 = px.pie(employer_category_count, employer_category_count.index,employer_category_count.values)
st.plotly_chart(fig1, use_container_width=True)