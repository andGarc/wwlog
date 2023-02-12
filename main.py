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

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)





