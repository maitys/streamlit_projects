# Contents of ~/my_app/main_page.py
import streamlit as st
import pandas as pd
st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

df = pd.DataFrame([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], columns=['A'])

name = st.text_input("What's your name?")
st.dataframe(df)