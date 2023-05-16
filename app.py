import numpy as np
import pandas as pd
import streamlit as st
df = pd.DataFrame(np.random.randn(500,2) / [50, 50] + [37.76, -122.4], columns=['lat', 'lon'])
st.map(df)

#x = st.slider('Select a value')
#st.write(x, 'squared id', x * x)
