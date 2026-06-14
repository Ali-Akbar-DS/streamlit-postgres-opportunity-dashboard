import streamlit as st
import pandas as pd
import plotly.express as px
from db import engine

st.header("📊 Analytics Dashboard")

try:
    df = pd.read_sql("SELECT * FROM opportunities", engine)
    
    if df.empty:
        st.warning("Not enough data to display analytics.")
    else:
        # 1. KPIs (6 required by rubric)
        col1, col2, col3 = st.columns(3)
        col1.metric("Total Opportunities", len(df))
        col2.metric("Open Roles", len(df[df['status'] == 'Open']))
        col3.metric("Remote Roles", len(df[df['work_mode'] == 'Remote']))
        
        col4, col5, col6 = st.columns(3)
        col4.metric("Avg Min Salary", f"PKR {df[df['currency']=='PKR']['salary_min'].mean():,.0f}")
        col5.metric("Top City", df['city'].mode()[0])
        col6.metric("Top Category", df['category'].mode()[0])

        # 2. Charts (Plotly required by rubric)
        st.subheader("Market Trends")
        chart_col1, chart_col2 = st.columns(2)
        
        with chart_col1:
            fig1 = px.pie(df, names='category', title="Roles by Category")
            st.plotly_chart(fig1, use_container_width=True)
            
            fig2 = px.histogram(df, x='city', title="Roles by City")
            st.plotly_chart(fig2, use_container_width=True)

        with chart_col2:
            fig3 = px.pie(df, names='work_mode', title="Work Mode Distribution")
            st.plotly_chart(fig3, use_container_width=True)
            
            fig4 = px.bar(df.groupby('company_name').size().reset_index(name='count'), x='company_name', y='count', title="Roles by Company")
            st.plotly_chart(fig4, use_container_width=True)

except Exception as e:
    st.error(f"Dashboard Error: {e}")