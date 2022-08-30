import streamlit as st
from Models import Post
from typing import Callable


class FeedView:
    def __init__(self, get_feed_func: Callable[[], list]):
        posts = get_feed_func()
        for post in posts:
            _PostView(post)


class _PostView:
    def __init__(self, post: Post):
        st.write(f"**{post.creator_name}**: {post.content} | _{post.posting_date}_")
