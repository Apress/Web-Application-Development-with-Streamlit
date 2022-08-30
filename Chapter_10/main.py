import streamlit as st

st.title("Welcome, WWW")

url = "https://www.whatismyip-address.com"

script = f"""
<iframe src="{url}" height="500" width="500"></iframe>
"""

st.write(script, unsafe_allow_html=True)
st.write(f"Check out your [public IP]({url})")
