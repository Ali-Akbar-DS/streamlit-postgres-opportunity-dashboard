import streamlit as st
import pandas as pd
from sqlalchemy import text
from db import engine

st.header("📝 Add a New Opportunity")
st.markdown("Use this form to insert a new internship or job record into the database.")

# clear_on_submit ensures the form resets after a successful save
with st.form("add_opportunity_form", clear_on_submit=True):
    st.subheader("Job Details")
    col1, col2 = st.columns(2)
    
    with col1:
        company_name = st.text_input("Company Name*")
        job_title = st.text_input("Job Title*")
        category = st.selectbox("Category", ["Data Science", "AI", "Web Development", "Software Engineering", "Cyber Security"])
        city = st.text_input("City")
        country = st.text_input("Country", value="Pakistan")
        
    with col2:
        work_mode = st.selectbox("Work Mode", ["Remote", "Onsite", "Hybrid"])
        experience_level = st.selectbox("Experience Level", ["Internship", "Entry Level", "Mid Level", "Senior Level"])
        status = st.selectbox("Status", ["Open", "Closed", "Shortlisted", "Expired"])
        application_deadline = st.date_input("Application Deadline")

    required_skills = st.text_area("Required Skills (Comma separated)")
    
    st.divider()
    st.subheader("Salary Details (Optional)")
    sal_col1, sal_col2, sal_col3 = st.columns(3)
    with sal_col1:
        salary_min = st.number_input("Min Salary", min_value=0, step=5000)
    with sal_col2:
        salary_max = st.number_input("Max Salary", min_value=0, step=5000)
    with sal_col3:
        currency = st.selectbox("Currency", ["PKR", "USD", "EUR", "GBP"])

    # The submit button
    submitted = st.form_submit_button("Save to Database", type="primary", use_container_width=True)

    # Database Insertion Logic
    if submitted:
        if not company_name or not job_title:
            st.error("⚠️ Company Name and Job Title are mandatory fields!")
        else:
            try:
                with engine.begin() as conn:
                    query = text("""
                        INSERT INTO opportunities 
                        (company_name, job_title, category, city, country, work_mode, experience_level, status, application_deadline, required_skills, salary_min, salary_max, currency)
                        VALUES 
                        (:company, :title, :category, :city, :country, :mode, :exp, :status, :deadline, :skills, :smin, :smax, :curr)
                    """)
                    conn.execute(query, {
                        "company": company_name, "title": job_title, "category": category, 
                        "city": city, "country": country, "mode": work_mode, 
                        "exp": experience_level, "status": status, "deadline": application_deadline,
                        "skills": required_skills, "smin": salary_min, "smax": salary_max, "curr": currency
                    })
                st.success(f"✅ Successfully added **{job_title}** at **{company_name}** to the database!")
            except Exception as e:
                st.error(f"🚨 Database Error: {e}")