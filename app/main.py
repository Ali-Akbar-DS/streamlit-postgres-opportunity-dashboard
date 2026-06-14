import streamlit as st
import pandas as pd
from auth import login_system
from db import engine

# 1. Page Configuration MUST be the first Streamlit command
st.set_page_config(
    page_title="Opportunity Tracker",
    page_icon="💼",
    layout="wide",
    initial_sidebar_state="expanded"
)

# 2. Initialize the login system in the sidebar
login_system()

# 3. Homepage Content
st.title("🎓 Department Internship & Job Tracking Hub")
st.markdown("""
Welcome to the central dashboard for managing student opportunities. 
Use the navigation menu on the left to access different modules:
* **Add Opportunity:** Insert new roles into the database.
* **View & Search:** Filter and find specific records.
* **Analytics Dashboard:** View market trends and salary data.
""")

st.info(f"Current Access Level: **{st.session_state.get('role', 'Viewer')}**")

st.divider()

# 4. Quick System Status Check
st.subheader("📌 System Status")
try:
    # A quick database query to prove the connection is alive on the homepage
    query = "SELECT COUNT(*) as total FROM opportunities"
    df = pd.read_sql(query, engine)
    total_records = df['total'][0]
    
    st.metric("Total Opportunities in Database", total_records)
    st.success("✅ Database connection is active and healthy.")
except Exception as e:
    st.warning("Database is currently initializing or empty. Add records to see stats.")