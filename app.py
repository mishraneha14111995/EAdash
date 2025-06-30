import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_page_config(page_title="HR Analytics Dashboard", layout="wide")

# Load the dataset
@st.cache_data
df= pd.read_csv("EA.csv")

# Sidebar Filters
st.sidebar.header("Filter Data")
departments = st.sidebar.multiselect("Department", options=df["Department"].unique(), default=df["Department"].unique())
job_roles = st.sidebar.multiselect("Job Role", options=df["JobRole"].unique(), default=df["JobRole"].unique())
genders = st.sidebar.multiselect("Gender", options=df["Gender"].unique(), default=df["Gender"].unique())

df_filtered = df[
    (df["Department"].isin(departments)) &
    (df["JobRole"].isin(job_roles)) &
    (df["Gender"].isin(genders))
]

# Create Tabs
tab1, tab2, tab3 = st.tabs(["Overview", "Macro Analysis", "Micro Analysis"])

with tab1:
    st.title("Overview Dashboard")
    st.markdown("### 🎯 Attrition Overview")
    st.markdown("Shows overall attrition distribution in the organization.")
    fig1 = px.pie(df_filtered, names='Attrition', title='Attrition Distribution')
    st.plotly_chart(fig1, use_container_width=True)

    st.markdown("### 📊 Attrition by Department")
    attr_by_dept = df_filtered.groupby(['Department', 'Attrition']).size().reset_index(name='Count')
    fig2 = px.bar(attr_by_dept, x='Department', y='Count', color='Attrition', barmode='group')
    st.plotly_chart(fig2, use_container_width=True)

    st.markdown("### 👥 Gender Distribution")
    fig3 = px.pie(df_filtered, names='Gender', title='Gender Split')
    st.plotly_chart(fig3, use_container_width=True)

with tab2:
    st.header("Macro-Level Analysis")

    st.markdown("### 🔥 Correlation Heatmap")
    corr = df_filtered.select_dtypes(include=np.number).corr()
    fig4, ax = plt.subplots(figsize=(14, 10))
    sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f", ax=ax)
    st.pyplot(fig4)

    st.markdown("### 💼 Income by Department")
    fig5 = px.box(df_filtered, x="Department", y="MonthlyIncome", color="Attrition")
    st.plotly_chart(fig5, use_container_width=True)

    st.markdown("### 📅 Age Distribution")
    fig6 = px.histogram(df_filtered, x='Age', color='Attrition', barmode='overlay')
    st.plotly_chart(fig6, use_container_width=True)

    st.markdown("### 📚 Education Field Breakdown")
    edu_count = df_filtered['EducationField'].value_counts().reset_index()
    fig7 = px.bar(edu_count, x='index', y='EducationField', labels={"index": "Field", "EducationField": "Count"})
    st.plotly_chart(fig7, use_container_width=True)

    st.markdown("### 🔄 Business Travel & Attrition")
    fig8 = px.histogram(df_filtered, x='BusinessTravel', color='Attrition')
    st.plotly_chart(fig8, use_container_width=True)

    st.markdown("### ⏰ Overtime Impact")
    fig9 = px.histogram(df_filtered, x='OverTime', color='Attrition')
    st.plotly_chart(fig9, use_container_width=True)

with tab3:
    st.header("Micro-Level Deep Dive")

    st.markdown("### 💸 Income vs Job Role")
    fig10 = px.box(df_filtered, x='JobRole', y='MonthlyIncome', color='Attrition')
    st.plotly_chart(fig10, use_container_width=True)

    st.markdown("### 📈 Years at Company")
    fig11 = px.histogram(df_filtered, x='YearsAtCompany', color='Attrition')
    st.plotly_chart(fig11, use_container_width=True)

    st.markdown("### 📊 Age vs Monthly Income")
    fig12 = px.scatter(df_filtered, x='Age', y='MonthlyIncome', color='Attrition')
    st.plotly_chart(fig12, use_container_width=True)

    st.markdown("### 🧭 Job Satisfaction vs Attrition")
    fig13 = px.histogram(df_filtered, x='JobSatisfaction', color='Attrition')
    st.plotly_chart(fig13, use_container_width=True)

    st.markdown("### 📈 Performance Rating")
    fig14 = px.histogram(df_filtered, x='PerformanceRating', color='Attrition')
    st.plotly_chart(fig14, use_container_width=True)

    st.markdown("### 🧮 Education vs Income")
    fig15 = px.box(df_filtered, x='Education', y='MonthlyIncome', color='Attrition')
    st.plotly_chart(fig15, use_container_width=True)
