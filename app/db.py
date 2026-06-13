import streamlit as st
from sqlalchemy import create_engine
import os
from dotenv import load_dotenv

# Load environment variables (useful for local testing outside Docker)
load_dotenv()

# Use st.cache_resource to handle connection efficiently as per assignment requirements
@st.cache_resource
def init_connection():
    db_user = os.getenv("DB_USER", "app_user")
    db_pass = os.getenv("DB_PASSWORD", "app_password")
    db_host = os.getenv("DB_HOST", "postgres_db")
    db_port = os.getenv("DB_PORT", "5432")
    db_name = os.getenv("DB_NAME", "student_opportunities_db")
    
    # Create the SQLAlchemy engine using psycopg2 driver
    db_url = f"postgresql+psycopg2://{db_user}:{db_pass}@{db_host}:{db_port}/{db_name}"
    engine = create_engine(db_url)
    return engine

# Expose the engine to be imported by other files
engine = init_connection()