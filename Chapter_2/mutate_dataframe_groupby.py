import streamlit as st
import pandas as pd
import numpy as np

df = pd.DataFrame(
    np.random.randn(12, 3),
    columns=('Score 1','Score 2','Score 3')
                  )

df['Name'] = pd.DataFrame(['John','Alex','Jessica','John','Alex','John',
'Jessica','John','Alex','Alex','Jessica','Jessica'])

df['Category'] = pd.DataFrame(['B','A','D','C','C','A',
'B','C','B','A','A','D'])

st.subheader('Original dataframe')
st.write(df)

st.subheader('Mutated dataframe')
st.write(df.groupby(['Name','Category']).first())
