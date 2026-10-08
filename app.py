from pathlib import Path
import streamlit as st

st.set_page_config(
    page_title="高性价比人生指南",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html = Path(__file__).with_name("HowToLiveBetter.html").read_text(encoding="utf-8")
st.html(html, unsafe_allow_javascript=True)
