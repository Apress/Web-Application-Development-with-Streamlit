import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame(data={'Exam':['Exam 1','Exam 2','Exam 3'],
'Jessica':[77,76,87],'John':[56,97,95],'Alex':[87,82,93]}
                  )

df.set_index('Exam').plot(kind='line',xlabel='Exam',ylabel='Score',subplots=True)
st.pyplot(plt)
