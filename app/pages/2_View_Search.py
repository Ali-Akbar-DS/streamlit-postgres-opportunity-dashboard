import streamlit as st
import pandas as pd
from db import engine

st.header("🔍 View & Search Opportunities")

# Search and Filter Layout
col1, col2 = st.columns([2, 1])
with col1:
    search_term = st.text_input("Search by Job Title or Company Name")
with col2:
    status_filter = st.selectbox("Filter by Status", ["All", "Open", "Closed", "Shortlisted", "Expired"])

try:
    # Pull data using Pandas directly from the SQLAlchemy engine
    query = "SELECT * FROM opportunities ORDER BY created_at DESC"
    df = pd.read_sql(query, engine)

    # Apply search filter
    if search_term:
        df = df[df['job_title'].str.contains(search_term, case=False, na=False) | 
                df['company_name'].str.contains(search_term, case=False, na=False)]
    
    # Apply status filter
    if status_filter != "All":
        df = df[df['status'] == status_filter]

    st.dataframe(df, use_container_width=True, hide_index=True)
    st.metric("Total Records Found", len(df))

except Exception as e:
    st.error(f"Failed to load data: {e}")