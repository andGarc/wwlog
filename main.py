# main.py
import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
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

multi = '''**WW Sessions**  
Whitewater Log  
'''

st.markdown(multi)
st.markdown(f"### {get_total_sessions_ww()} sessions")
st.markdown(f"Last on the river on **{get_last_on_river_ww()}**")
"---"

