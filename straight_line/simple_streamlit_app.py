# simple_streamlit_app.py
"""
A simple streamlit app
run the app by installing streamlit with pip and typing
> streamlit run simple_streamlit_app.py
"""

import streamlit as st

st.title('Simple Streamlit App')

x = st.slider('x')
st.write(x, 'squared is', x * x)

s = st.text_input('Type a name in the box below')
st.write(f'Hello {s}')

if st.button('Say hello'):
     st.write('Why hello there')
else:
     st.write('Goodbye')