import streamlit as st
import pandas as pd

def load_csv():
    uploaded_file = st.file_uploader("Choose a CSV file", type="csv")
    if uploaded_file is not None:
        # Read the CSV file into a Pandas DataFrame
        return pd.read_csv(uploaded_file)
    return None
