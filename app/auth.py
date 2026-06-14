import streamlit as st

def login_system():
    if "role" not in st.session_state:
        st.session_state["role"] = "Viewer"

    st.sidebar.subheader("🔐 Access Control")
    user_role = st.sidebar.radio("Select Role", ["Viewer", "Admin"], index=0 if st.session_state["role"] == "Viewer" else 1)
    
    if user_role != st.session_state["role"]:
        st.session_state["role"] = user_role
        st.rerun()

def is_admin():
    return st.session_state.get("role") == "Admin"