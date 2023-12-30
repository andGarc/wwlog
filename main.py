# main.py
import streamlit as st
from db import get_total_sessions_ww, get_last_on_river_ww

st.set_page_config(
    page_title="AG Logs", layout="centered"
)

st.write("""
# AG Logs  
Select a log on the right to start.  
See summaries below.  
""")  
"---"

st.markdown("### WW Sesssions")
st.markdown(f"Total sessions: **{get_total_sessions_ww()}**")
st.markdown(f"Last on the river: **{get_last_on_river_ww()}**")
"---"