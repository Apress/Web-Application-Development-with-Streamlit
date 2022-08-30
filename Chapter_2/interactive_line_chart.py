import streamlit as st
import pandas as pd
import plotly.graph_objects as go

df = pd.DataFrame(data={'Exam':['Exam 1','Exam 2','Exam 3'],
'Jessica':[77,76,87],'John':[56,97,95],'Alex':[87,82,93]}
                  )
fig = go.Figure(data=[
    go.Line(name='Jessica', x=df['Exam'], y=df['Jessica']),
    go.Line(name='John', x=df['Exam'], y=df['John']),
    go.Line(name='Alex', x=df['Exam'], y=df['Alex'])
])

fig.update_layout(
    xaxis_title='Exam',
    yaxis_title='Score',
    legend_title='Name',
)

st.plotly_chart(fig)
