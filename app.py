import streamlit as st
import pandas as pd

st.title("Unemployment Analysis in India")

df = pd.read_csv("unemployment in india.csv")

# remove extra spaces
df.columns = df.columns.str.strip()

# show data
st.write(df.head())

# line chart
st.line_chart(
    df["Estimated Unemployment Rate (%)"]
)