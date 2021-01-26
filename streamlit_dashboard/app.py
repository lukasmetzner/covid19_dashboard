import streamlit as st
import pandas as pd
import numpy as np
import scipy.signal as sig
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import plotly.express as px

st.set_page_config(layout="wide")
st.write("Hopkins Covid19 Dashboard")


df_cases = pd.read_csv("../cases_transformed.csv")
df_deaths = pd.read_csv("../deaths_transformed.csv")
df_recovered = pd.read_csv("../recovered_transformed.csv")

st.sidebar.write("Savitzky–Golay filter parameters")
odd_numbers_window = [x for x in range(0, 100) if x % 2 == 1]
window_length = st.sidebar.select_slider("Windows length", options=odd_numbers_window, value=23)
odd_numbers_poly = [x for x in range(0, 50) if x % 2 == 1]
poly_order = st.sidebar.select_slider("Poly order", options=odd_numbers_poly, value=5)

raw, smoothed = st.beta_columns(2)

try:
    fig = make_subplots(rows=3, cols=2)
    with raw:
        st.plotly_chart(px.line(df_cases, x="date", y="new_cases"), use_container_width=True)
        st.plotly_chart(px.line(df_deaths, x="date", y="new_deaths"), use_container_width=True)
        st.plotly_chart(px.line(df_recovered, x="date", y="new_recovered"), use_container_width=True)

    with smoothed:
        st.plotly_chart(px.line(df_cases, x="date", y=sig.savgol_filter(df_cases.new_cases, window_length, poly_order)), use_container_width=True)
        st.plotly_chart(px.line(df_deaths, x="date", y=sig.savgol_filter(df_deaths.new_deaths, window_length, poly_order)), use_container_width=True)
        st.plotly_chart(px.line(df_recovered, x="date", y=sig.savgol_filter(df_recovered.new_recovered, window_length, poly_order)), use_container_width=True)
except Exception as e:
    st.write(e)

def divide(x, y):
    try:
        return x / y
    except:
        return 0