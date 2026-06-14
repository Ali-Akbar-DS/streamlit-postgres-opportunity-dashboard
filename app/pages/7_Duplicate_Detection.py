import streamlit as st
import pandas as pd
from db import engine

st.header("👯 Duplicate Detection")
st.markdown("This tool scans the database for potential duplicate entries based on the **Company Name**, **Job Title**, and **City**.")

try:
    # Fetch all records
    df = pd.read_sql("SELECT * FROM opportunities", engine)
    
    if df.empty:
        st.info("The database is currently empty.")
    else:
        # Find duplicates based on specific columns
        duplicates = df[df.duplicated(subset=['company_name', 'job_title', 'city'], keep=False)]
        
        if not duplicates.empty:
            st.warning(f"Found {len(duplicates)} potential duplicate records!")
            # Sort to show duplicates next to each other
            duplicates_sorted = duplicates.sort_values(by=['company_name', 'job_title'])
            st.dataframe(duplicates_sorted[['opportunity_id', 'company_name', 'job_title', 'city', 'status', 'created_at']], use_container_width=True)
            
            st.info("💡 To remove a duplicate, note its `opportunity_id` and use the **Delete Opportunity** page.")
        else:
            st.success("Great news! No duplicate records detected in the database.")

except Exception as e:
    st.error(f"Error running duplicate detection: {e}")