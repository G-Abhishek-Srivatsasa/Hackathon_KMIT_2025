import streamlit as st
import auth

def show_login_page():
    st.markdown("<h2 style='text-align:center;'>🔐 Login Page</h2>", unsafe_allow_html=True)

    option = st.radio("Choose an option:", ["Login", "Signup"])

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if option == "Signup":
        if st.button("Sign Up"):
            if auth.signup(username, password):
                st.success("Signup successful! Please login now.")
            else:
                st.error("Username already exists.")

    if option == "Login":
        if st.button("Login"):
            if auth.login(username, password):
                st.session_state["logged_in"] = True
                st.success("Login successful!")
                st.rerun()
            else:
                st.error("Invalid username or password.")
