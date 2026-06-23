import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Unemployment Analysis in India")

df = pd.read_csv("unemployment in india.csv")

st.write(df.head())

plt.figure(figsize=(10,5))
plt.plot(df["Date"], df["Estimated Unemployment Rate (%)"])

plt.xticks(rotation=45)

st.pyplot(plt)