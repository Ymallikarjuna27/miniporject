import streamlit as st
import pandas as pd

st.title("Mini Data Processing Tool")

# File Upload
uploaded_file = st.file_uploader(
    "Upload input CSV file",
    type=["csv"]
)

if uploaded_file is not None:
    # Read uploaded file
    df = pd.read_csv(uploaded_file)

    st.subheader("Uploaded Data")
    st.dataframe(df)

    # Transform data
    df["result"] = df["marks"].apply(
        lambda x: "Pass" if x >= 70 else "Fail"
    )

    average_marks = round(df["marks"].mean(), 2)

    st.subheader("Processed Data")
    st.dataframe(df)

    st.subheader("Summary")
    st.write("Average Marks:", average_marks)

    # Download processed file
    csv_data = df.to_csv(index=False).encode("utf-8")

    st.download_button(
        label="Download Processed CSV",
        data=csv_data,
        file_name="processed_data.csv",
        mime="text/csv"
    )
