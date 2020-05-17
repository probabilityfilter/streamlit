# simple_streamlit_app.py
"""
A simple streamlit app
run the app by installing streamlit with pip and typing
> streamlit run simple_streamlit_app.py
"""

import numpy as np
import streamlit as st
from bokeh.plotting import figure

st.title('Simple Classification')

slope = st.slider('Slope')
intercept = st.slider('Intercept')

x = np.arange(-3.0, 3.0, 0.1)
y = slope * x + intercept

p = figure(
    title="Mohr's Circle",
    x_axis_label="stress",
    y_axis_label="shear",
    match_aspect=True,
    tools="pan,reset,save,wheel_zoom",
)

p.line(x, y, color="#ff7f0e", line_width=3, line_alpha=0.6)

p.xaxis.fixed_location = 0
p.yaxis.fixed_location = 0

st.bokeh_chart(p)