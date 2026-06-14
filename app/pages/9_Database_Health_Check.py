import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import engine

st.header("🩺 Database Health Check")
st.markdown("Diagnostic page to verify PostgreSQL connection and table status.")

try:
    with engine.connect() as conn:
        # 1. Test Connection & Version
        version_result = conn.execute(text("SELECT version();")).fetchone()
        st.success(f"✅ **Connected to:** {version_result[0]}")
        
        st.divider()
        
        # 2. Count Rows
        count_result = conn.execute(text("SELECT COUNT(*) FROM opportunities;")).fetchone()
        total_rows = count_result[0]
        st.metric("Total Records in Database", total_rows)
        
        if total_rows > 0:
            # 3. Latest Record
            st.subheader("Latest Inserted Record")
            latest_query = "SELECT opportunity_id, company_name, job_title, created_at FROM opportunities ORDER BY created_at DESC LIMIT 1"
            df_latest = pd.read_sql(latest_query, conn)
            st.dataframe(df_latest, hide_index=True)
            
        # 4. Table Columns Schema
        st.subheader("Table Schema (opportunities)")
        schema_query = """
            SELECT column_name, data_type, character_maximum_length 
            FROM information_schema.columns 
            WHERE table_name = 'opportunities';
        """
        df_schema = pd.read_sql(schema_query, conn)
        st.dataframe(df_schema, use_container_width=True, hide_index=True)

except Exception as e:
    st.error("🚨 **Database Connection Failed!**")
    st.error(str(e))
    st.info("Troubleshooting: Check if the `postgres_db` Docker container is running and port 5432 is mapped correctly.")