import streamlit as st
from datetime import datetime

#Expander in sidebar
st.sidebar.subheader('Expander')
with st.sidebar.expander('Time'):
    time = datetime.now().strftime("%H:%M:%S")
    st.write('**%s**' % (time))

#Columns in sidebar
st.sidebar.subheader('Columns')
col1, col2 = st.sidebar.columns(2)
with col1:
    option_1 = st.selectbox('Please select option 1',['A','B'])
with col2:
    option_2 = st.radio('Please select option 2',['A','B'])

#Container in sidebar
container = st.sidebar.container()
container.subheader('Container')
option_3 = container.slider('Please select option 3')
st.sidebar.warning('Elements outside of container will be displayed externally')
container.info('**Option 3:** %s' % (option_3))

#Expander in main body
st.subheader('Expander')
with st.expander('Time'):
    time = datetime.now().strftime("%H:%M:%S")
    st.write('**%s**' % (time))

#Columns in main body
st.subheader('Columns')
col1, col2 = st.columns(2)
with col1:
    option_4 = st.selectbox('Please select option 4',['A','B'])
with col2:
    option_5 = st.radio('Please select option 5',['A','B'])

#Container in main body
container = st.container()
container.subheader('Container')
option_6 = container.slider('Please select option 6')
st.warning('Elements outside of container will be displayed externally')
container.info('**Option 6:** %s' % (option_6))
