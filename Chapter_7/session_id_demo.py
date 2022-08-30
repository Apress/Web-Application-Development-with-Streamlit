import streamlit as st
from streamlit.report_thread import get_report_ctx
from streamlit.server.server import Server

all_sessions = Server.get_current()._session_info_by_id

session_id = get_report_ctx().session_id
session_number = list(all_sessions.keys()).index(session_id) + 1

st.title("Session ID #"+str(session_number))
st.header("Id of this session is: " + session_id)
st.subheader("All sessions ("+str(len(all_sessions))+") :")
st.write(all_sessions)
