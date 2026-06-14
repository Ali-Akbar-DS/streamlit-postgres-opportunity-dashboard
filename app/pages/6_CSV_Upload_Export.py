import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import engine

st.header("📂 CSV Upload & Export")

st.subheader("Export Data")
try:
    df_export = pd.read_sql("SELECT * FROM opportunities", engine)
    csv = df_export.to_csv(index=False).encode('utf-8')
    st.download_button("Download Current Database as CSV", csv, "opportunities.csv", "text/csv")
except Exception as e:
    st.error("Failed to load export data.")

st.divider()

st.subheader("Upload Data (Bulk Insert)")
uploaded_file = st.file_uploader("Upload a CSV file to add new opportunities", type=["csv"])

if uploaded_file is not None:
    df_upload = pd.read_csv(uploaded_file)
    st.write("Preview of Uploaded Data:")
    st.dataframe(df_upload.head())
    
    if st.button("Insert into Database"):
        try:
            df_upload.to_sql('opportunities', engine, if_exists='append', index=False)
            st.success(f"Successfully inserted {len(df_upload)} records!")
        except Exception as e:
            st.error(f"Failed to insert records. Ensure columns match the database schema. Error: {e}")