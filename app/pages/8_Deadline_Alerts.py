import streamlit as st
import pandas as pd
from db import engine

st.header("⏰ Deadline Alerts")

try:
    # Use Pandas to filter dates to avoid complex SQL timezone issues
    df = pd.read_sql("SELECT * FROM opportunities WHERE application_deadline IS NOT NULL", engine)
    df['application_deadline'] = pd.to_datetime(df['application_deadline'])
    
    today = pd.to_datetime("today")
    seven_days_from_now = today + pd.Timedelta(days=7)
    
    # Filter for approaching and expired
    approaching = df[(df['application_deadline'] >= today) & (df['application_deadline'] <= seven_days_from_now)]
    expired = df[df['application_deadline'] < today]
    
    st.subheader("🚨 Closing within 7 Days")
    if not approaching.empty:
        st.dataframe(approaching[['company_name', 'job_title', 'application_deadline']], use_container_width=True)
    else:
        st.success("No immediate deadlines.")
        
    st.subheader("❌ Expired Opportunities")
    if not expired.empty:
        st.dataframe(expired[['company_name', 'job_title', 'application_deadline', 'status']], use_container_width=True)
    else:
        st.info("No expired records found.")

except Exception as e:
    st.error(f"Failed to fetch alerts: {e}")