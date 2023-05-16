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
