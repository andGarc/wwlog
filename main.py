# main.py

import streamlit as st
from deta import Deta

st.sidebar.markdown('# Main')

st.write("""
# Whitewater Log 🌊
""")

# Connect to Deta Base with your Project Key
deta = Deta(st.secrets['deta_key'])

# Create a new database "wwlog-db"
db = deta.Base("wwlog-db")

# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items

# last session
last_session = db_content[len(db_content) - 1]

"---"
st.markdown(f"**{len(db_content)}** session so far in 2023.")

"---"





