# main.py
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime
from db import load_data, get_total_sessions_ww_curr_year, get_last_on_river_ww

st.set_page_config(
    page_title="AG Logs", layout="centered"
)

# load data 
data_df = load_data()

st.write("""
# AG Logs  
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

st.markdown(f"Last on the river on **{get_last_on_river_ww(data_df)}**")

data_df['Date'] = pd.to_datetime(data_df['Date'])

# Group by month and category, then count occurrences
data_df['Month'] = data_df['Date'].dt.to_period('M')
grouped = data_df.groupby(['Month', 'River']).size().unstack()

# Plot the results
st.markdown('**Sessions by Month**')
fig, ax = plt.subplots(figsize=(10, 7))
grouped.plot(kind='bar', stacked=True, ax=ax)
plt.xlabel('Month')

# Show the plot in Streamlit
st.pyplot(fig)
"---"

