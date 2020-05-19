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

angle = st.sidebar.slider('Angle', 0, 180, 45)
intercept = st.sidebar.slider('Intercept', -5.0, 5.0, 0.0, 0.1)

x = np.arange(-5.0, 5.0, 0.1)
y = np.tan(np.radians(angle)) * x + intercept

p = figure(
    title="Staright Line",
    x_axis_label="x-axis",
    y_axis_label="y-axis",
    match_aspect=False,
    tools="pan,reset,save,wheel_zoom",
    x_range=(-5, 5),
    y_range=(-5, 5)
)

p.line(x, y, color="#ff7f0e", line_width=3, line_alpha=0.6)

p.xaxis.fixed_location = 0
p.yaxis.fixed_location = 0

st.bokeh_chart(p)