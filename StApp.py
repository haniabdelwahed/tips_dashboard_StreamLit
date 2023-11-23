import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px

st.set_page_config(page_title="Tips Dashboard", layout="wide", initial_sidebar_state="auto")

df = pd.read_csv('tips.csv')

st.sidebar.header("Tips Dashboard")
st.sidebar.image('OIP.jpg')
st.sidebar.write("This is a test for Stream Lit using the Tips dataset from Kuggle for educational purpose only.")
st.sidebar.write("")
st.sidebar.write("Filter your data:")
cat_filter = st.sidebar.selectbox("Category", [None, "sex", "smoker", "day", "time"])
num_filter = st.sidebar.selectbox("Size By", [None, "total_bill", "tip"])
facet_row_filter = st.sidebar.selectbox("Category Row", [None, "sex", "smoker", "day", "time"])
facet_col_filter = st.sidebar.selectbox("Category Column", [None, "sex", "smoker", "day", "time"])



st.sidebar.write("")
st.sidebar.markdown("Made By Eng. [Hani Abdelwahed](https://www.linkedin.com/in/haniabdelwahed/)")

# body

# row 1

f1, f2, f3, f4 = st.columns(4)
f1.metric("Max. Total bill", df["total_bill"].max())
f2.metric("Max. tip", df["tip"].max())
f3.metric("Min. Total bill", df["total_bill"].min())
f4.metric("Min. tip", df["tip"].min())



# row 2
# st.subheader("Total Bills vs Tips")
fig = px.scatter(data_frame= df, x= "total_bill", y= "tip", color=cat_filter, size=num_filter, title="Total Bills vs Tips", facet_col=facet_col_filter, facet_row=facet_row_filter)

st.plotly_chart(fig, use_container_width=True)

c1, c2, c3 = st.columns((4, 3, 3))
with c1:
    st.text("Sex vs Total Bills")
    fig = px.bar(data_frame=df, x="sex", y="total_bill", color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
with c2:
    st.text("Smoker/NoSmoker vs tip")
    fig = px.pie(data_frame=df, names="smoker", values="tip", color=cat_filter)
    st.plotly_chart(fig, use_container_width=True)
with c3:
    st.text("Days vs tip")
    fig = px.pie(data_frame=df, names="day", values="tip", color=cat_filter, hole=0.4)
    st.plotly_chart(fig, use_container_width=True)