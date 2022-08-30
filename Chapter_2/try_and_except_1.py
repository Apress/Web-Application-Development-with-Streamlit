import streamlit as st

col1, col2 = st.columns(2)

with col1:
    number_1 = st.number_input('Please enter the first number',value=0,step=1)
with col2:
    number_2 = st.number_input('Please enter the second number',value=0,step=1)

try:
    st.info('**%s/%s=** %s' % (number_1,number_2,number_1/number_2))
except ZeroDivisionError:
    st.error('Cannot divide by zero')
except:
    pass
