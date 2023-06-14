import streamlit as st
from send_email import send_email

st.title("Contact Me")

with st.form(key="email_forms", clear_on_submit=True):
    user_email = st.text_input("Your email address:", placeholder="ex., user@example.com")
    raw_message = st.text_area("Your message:")
    message = f"""\
Subject: Portfolio App

From: {user_email}
{raw_message}
"""
    button = st.form_submit_button("Submit")
    if button:
        send_email(message)
        st.info("Your email was sent successfully.")
