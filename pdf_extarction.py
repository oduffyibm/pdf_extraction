import streamlit as st
import pandas as pd
from io import StringIO

uploaded_file = st.file_uploader("Choose a file")

if uploaded_file:
    st.write("filename:", uploaded_file.name)