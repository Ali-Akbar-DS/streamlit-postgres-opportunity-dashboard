import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import engine

st.header("🗑️ Delete Opportunity")

try:
    df = pd.read_sql("SELECT opportunity_id, company_name, job_title FROM opportunities", engine)
    
    if df.empty:
        st.info("The database is currently empty.")
    else:
        options = {f"ID: {row['opportunity_id']} - {row['job_title']} at {row['company_name']}": row['opportunity_id'] for _, row in df.iterrows()}
        selected_record = st.selectbox("Select Record to Delete", list(options.keys()))
        selected_id = options[selected_record]

        st.warning(f"Are you sure you want to permanently delete: **{selected_record}**?")
        
        if st.button("🚨 Confirm Deletion", type="primary"):
            with engine.begin() as conn:
                query = text("DELETE FROM opportunities WHERE opportunity_id = :id")
                conn.execute(query, {"id": int(selected_id)})
            st.success("Record deleted successfully.")
            st.rerun()

except Exception as e:
    st.error(f"An error occurred: {e}")