import streamlit as st
from PIL import Image
icon = Image.open('favicon.ico')

st.set_page_config(
    page_title='Hello world',
    page_icon=icon,
    layout='centered',
    initial_sidebar_state='auto',
    menu_items={
        'Get Help': 'https://streamlit.io/',
        'Report a bug': 'https://github.com',
        'About': 'About your application: **Hello world**'
        }
)

st.sidebar.title('Hello world')
st.title('Hello world')
