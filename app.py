import streamlit as st 

x = st.slider('Select a value')
st.write(x, 'squared is', x*x)

st.title("this is the app title")
st.markdown("this is the markdown")
st.header("this is the header")
st.subheader("this is the subheader")
st.caption("this is the caption")
st.code("x=2023")
st.latex(r'''
a + a r ^1+ a r^2 + a r^3 ''')

import pandas as pd
import numpy as np
df - pd.DataFrame(np.random.randn(500,2) / [50, 50] + [37.76, -122.4],
                  columns-['lat', 'lon'])
st.map(df)
