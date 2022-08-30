import streamlit as st
from typing import Callable


class Login:
    def __init__(self, on_login: Callable[[str, str], bool]):
        st.header("Login")
        username = st.text_input("Username")
        password = st.text_input("Password",type="password")

        if st.button("Login"):
            success = on_login(username, password)
            if success:
                st.success("Login successful")
            else:
                st.error("Incorrect username and password combination")
