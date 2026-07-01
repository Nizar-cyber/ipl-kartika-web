import streamlit as st
import streamlit.components.v1 as components
import pathlib

st.set_page_config(
    page_title="IPL Kartika Residence",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit default UI (menu, footer, header)
hide_style = """
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .block-container {padding: 0 !important; max-width: 100% !important;}
    .stApp {margin: 0; padding: 0;}
    iframe {border: none !important; width: 100% !important;}
    section[data-testid="stSidebar"] {display: none;}
</style>
"""
st.markdown(hide_style, unsafe_allow_html=True)

# Load HTML
html_file = pathlib.Path(__file__).parent / "iplweb.html"
html_content = html_file.read_text(encoding="utf-8")

# Render full-height
components.html(html_content, height=1000, scrolling=True)