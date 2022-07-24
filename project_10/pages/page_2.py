# Contents of ~/my_app/pages/page_2.py
import streamlit as st
from main_page import df, name
st.markdown("# Page 2 ❄️")
st.sidebar.markdown("# Page 2 ❄️")

st.dataframe(df)

st.markdown("## Hello %s" % name)