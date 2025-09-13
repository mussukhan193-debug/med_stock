import streamlit as st

st.title ("Medicine stock")
st.header ("Medicine list")

import pandas as pd

uploaded_file = st.file_uploader("upload an excel file", type=["xlsx","xls"])

if uploaded_file:
    df =pd.read_excel(uploaded_file)
    st.dataframe(df)

medicine_name=st.text_input("enter medicine name:")
fname =st.text_input("enter medicine sold:")
stockdata =st.selectbox("enter your stock:",(1,2,3,4,5,6,7,8,9,10.30))


button =st.button("done")
if button :
    st.markdown(f"""
    medicine name :{medicine_name}
    medicine sold :{fname}
    stock :{stockdata}""")











