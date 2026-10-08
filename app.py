from pathlib import Path
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="高性价比人生指南",
    page_icon="📖",
    layout="wide",
    initial_sidebar_state="collapsed",
)

html_path = Path(__file__).with_name("HowToLiveBetter.html")
html = html_path.read_text(encoding="utf-8")
components.html(html, height=900, scrolling=True)
