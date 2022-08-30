import streamlit as st
import psycopg2


@st.cache(allow_output_mutation=True,
          hash_funcs={"_thread.RLock": lambda _: None})
def init_connection():
    return psycopg2.connect(**st.secrets["db_postrgres"])


conn = init_connection()


def run_query(query_str):
    cur = conn.cursor()
    cur.execute(query_str)
    data = cur.fetchall()
    cur.close()
    return data


def run_query_with_context_manager(query_str):
    with conn.cursor() as cur:
        cur.execute(query_str)
        return cur.fetchall()


query = st.text_input("Query")

c1, c2 = st.columns(2)

output = None

with c1:
    if st.button("Run with context manager"):
        output = run_query_with_context_manager(query)
with c2:
    if st.button("Run without context manager"):
        output = run_query(query)

st.write(output)

