import streamlit as st
import pandas as pd

st.title("Mini GitHub Data Processing Tool")

@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/Ymallikarjuna27/miniporject/main/output/processed_data.csv"
    return pd.read_csv(url)

df = load_data()

st.subheader("Processed Data")
st.dataframe(df)

st.subheader("Summary")
st.write("Average Marks:", round(df["marks"].mean(), 2))
