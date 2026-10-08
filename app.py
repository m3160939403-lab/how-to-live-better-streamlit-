import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="高性价比人生指南",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

components.iframe(
    "https://eternity4719.github.io/HowToLiveBetter/",
    height=900,
    scrolling=True,
)
