import streamlit as st 
import pandas as pd
import numpy as np


df = pd.DataFrame(np.random.randn(500,2) / [100, 100] + [35.17, 129.07],
                  columns=['lat', 'lon'])
st.map(df)
