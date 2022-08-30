import streamlit as st
import pandas as pd

df = pd.DataFrame([["Adam", "01/01/1990", 2],
                   ["Sara", "01/01/1980", 1],
                   ["Bob", "01/01/1970", 1],
                   ["Alice", "01/01/2000", 3]
                   ], columns=["Name", "DOB", "Paygrade ID"])

st.table(df)

st.dataframe(df)