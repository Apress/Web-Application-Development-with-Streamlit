import streamlit as st


def get_state_value(key):
    return st.session_state.get(key)


def set_state_value(key, value):
    st.session_state[key] = value


st.title("Session State Management")
c1, c2, c3 = st.columns(3)

with c1:
    st.subheader("All")
    st.write(st.session_state)
with c2:
    st.subheader("Set Key")
    key = st.text_input("Key", key="KeyInput1")
    value = st.text_input("Value")

    if st.button("Set"):
        st.session_state[key] = value
        st.success("Success")
with c3:
    st.subheader("Get Key")
    key = st.text_input("Key", key="KeyInput2")

    if st.button("Get"):
        st.write(st.session_state.get(key))
