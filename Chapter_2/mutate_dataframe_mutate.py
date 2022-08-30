import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(4, 3),
    columns=('Column 1','Column 2','Column 3')
                  )
st.subheader('Original dataframe')
st.write(df)

st.subheader('Mutated dataframe')
st.write(df.assign(Column_4 = lambda x: df['Column 1']*2))
