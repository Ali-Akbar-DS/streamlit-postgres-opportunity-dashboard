import streamlit as st

def show_error(error_message):
    st.error(f"Database/Application Error: {error_message}")
    st.info("Tip: Check your docker-compose logs if the database connection failed.")