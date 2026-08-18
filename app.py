import streamlit as st

# Page setup
st.set_page_config(page_title="Login Page", page_icon="🔑")

st.title("Welcome to My App")
st.subheader("Login Portal")

# Login form
username = st.text_input("Username")
password = st.text_input("Password", type="password")

if st.button("Login"):
    if username == "admin" and password == "1234":
        st.success("Login successful!")
    else:
        st.error("Invalid credentials")

# Extra button (to test later)
if st.button("Refresh Page"):
    st.rerun()

