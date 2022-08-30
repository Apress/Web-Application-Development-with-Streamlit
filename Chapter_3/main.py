import streamlit as st
from Views import FeedView, AddPostView
from Services import get_feed, add_post

AddPostView(add_post)
st.write("___")
FeedView(get_feed)

