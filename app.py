import streamlit as st
import numpy as np
import pandas as pd

df = pd.DataFrame(np.rnadom.randn(500,2) / [50, 50] + [37.76, -122.4]),columns=['lat', 'lon'])
st.map(df)

#x = st.slider('Select a value')
#st.write(x, 'squared id', x * x)
