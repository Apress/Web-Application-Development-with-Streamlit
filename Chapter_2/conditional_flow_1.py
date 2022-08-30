import streamlit as st

def display_name():
    st.info('**Name:** %s' % (name))

name = st.text_input('Please enter your name')

if not name:
    st.error('No name entered')

if name:
    display_name()
