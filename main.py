# main.py
import streamlit as st
import pandas as pd
from datetime import datetime
from db import load_data, get_total_sessions_ww_curr_year, get_last_on_river_ww

st.set_page_config(
    page_title="AG Logs", layout="centered"
)

# load data 
data_df = load_data()

st.write("""
# AG Logs  
Select a log on the right to start.  
See summaries below.  
""")  
"---"

multi = f'''Whitewater Log  
**{datetime.now().year} WW Sessions**
'''

st.markdown(multi)
st.markdown(f"### {get_total_sessions_ww_curr_year(data_df)} sessions" 
            if get_total_sessions_ww_curr_year(data_df) > 1 
            else f"### {get_total_sessions_ww_curr_year(data_df)} session")

st.markdown(f"Last on the river on **{get_last_on_river_ww()}**")
"---"

