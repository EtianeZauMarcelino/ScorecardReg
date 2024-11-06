import streamlit as st
import pandas as pd
import numpy as np
import altair as alt

st.set_page_config(
    page_title="Ex-stream-ly Cool App",
    page_icon="🧊",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.logo(
    'LOGO-BRANCO-RGB.png',
    size="medium"
)

alt.themes.enable("dark")


st.markdown("# Main page 🎈")
st.sidebar.markdown("# Main page 🎈")

st.title('First page')

