import streamlit as st
import pandas as pd

df1 = pd.DataFrame(data={'Name':['Jessica','John','Alex'],
'Score 1':[77,56,87]}
                  )

df2 = pd.DataFrame(data={'Name':['Jessica','John','Alex'],
'Score 2':[76,97,82]}
                  )

st.subheader('Original dataframes')
st.write(df1)
st.write(df2)

st.subheader('Mutated dataframe')
st.write(df1.merge(df2,how='inner',on='Name'))
