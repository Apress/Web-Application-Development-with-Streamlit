import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.stocks()
st.title('DataFrame Demo')
program = st.sidebar.selectbox('Select program',['Dataframe Demo'])
code = st.sidebar.checkbox('Display code')
stocks = st.multiselect('Select stocks',df.columns[1:],[df.columns[1]])
st.subheader('Stock value')

# Mutating the dataframe to keep selected columns only
st.write(df[['date'] + stocks].set_index('date'))

# Creating a Plotly timeseries line chart
fig = px.line(df, x='date', y=stocks,
              hover_data={"date": "|%Y %b %d"}
              )

st.write(fig)

if code is True:
    st.code(
        """
import streamlit as st
import pandas as pd
import plotly.express as px

df = px.data.stocks()
st.title('DataFrame demo')
program = st.sidebar.selectbox('Select program',['Dataframe Demo'])
code = st.sidebar.checkbox('Display code')
stocks = st.multiselect('Select stocks',df.columns[1:],[df.columns[1]])
st.subheader('Stock value')
st.write(df[['date'] + stocks].set_index('date'))

fig = px.line(df, x='date', y=stocks,
              hover_data={"date": "|%Y %b %d"}
              )

st.write(fig)
        """
        )
