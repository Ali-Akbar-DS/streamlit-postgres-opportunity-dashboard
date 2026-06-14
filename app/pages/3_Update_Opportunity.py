import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import engine

st.header("✏️ Update Opportunity Status")

try:
    # Fetch current IDs and Job Titles for the dropdown
    df = pd.read_sql("SELECT opportunity_id, company_name, job_title, status FROM opportunities", engine)
    
    if df.empty:
        st.warning("No opportunities available to update.")
    else:
        # Create a dictionary to map a readable string to the actual ID
        options = {f"ID: {row['opportunity_id']} - {row['job_title']} at {row['company_name']} (Current: {row['status']})": row['opportunity_id'] for _, row in df.iterrows()}
        
        selected_record = st.selectbox("Select Record to Update", list(options.keys()))
        selected_id = options[selected_record]

        with st.form("update_form"):
            new_status = st.selectbox("Update Status", ["Open", "Closed", "Shortlisted", "Expired"])
            new_work_mode = st.selectbox("Update Work Mode", ["Remote", "Onsite", "Hybrid"])
            
            if st.form_submit_button("Update Database"):
                with engine.begin() as conn:
                    query = text("""
                        UPDATE opportunities 
                        SET status = :status, work_mode = :mode 
                        WHERE opportunity_id = :id
                    """)
                    conn.execute(query, {"status": new_status, "mode": new_work_mode, "id": selected_id})
                st.success(f"Successfully updated Record ID {selected_id}!")
                st.rerun()

except Exception as e:
    st.error(f"An error occurred: {e}")