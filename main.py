# main.py

import streamlit as st
import pandas as pd
from google.oauth2 import service_account
from gsheetsdb import connect

st.write("""
# Whitewater Log 🌊
""")

# with st.form('log_form'):
#     date = st.date_input('Date')

#     river = st.selectbox(
#         'Select a river section',
#         ('Little Falls', 'Great Falls', 'Upper Yough')
#     )

#     level = st.number_input('Level', 
#                         min_value=0.0, max_value=20000.0, step=0.01, value=3.0)

#     level_type = st.radio(
#                     'FT or CSF',
#                     options=('FT', 'CFS')
#                 )

#     notes = st.text_input('Notes', max_chars=200)

#     # Every form must have a submit button.
#     submitted = st.form_submit_button("Submit")
#     if submitted:
#         st.markdown(f"""
#             📝 **Entry**
#             - Date: `{date}`
#             - River: `{river}`
#             - Level: `{level} {level_type}`
#         """)

# Create a connection object.
credentials = service_account.Credentials.from_service_account_info(
    st.secrets["gcp_service_account"],
    scopes=[
        "https://www.googleapis.com/auth/spreadsheets",
    ],
)
conn = connect(credentials=credentials)

# Perform SQL query on the Google Sheet.
# Uses st.cache_data to only rerun when the query changes or after 10 min.
@st.cache_data(ttl=600)
def run_query(query):
    rows = conn.execute(query, headers=1)
    rows = rows.fetchall()
    st.success("Fetched data from GSheets!")
    
    date = []
    river = []
    level = []
    level_type = []
    for row in rows:
        date.append(row.date)
        river.append(row.river)
        level.append(row.level)
        level_type.append(row.level_type)

    rows_dict = {'date':date, 'river':river, 
                'level':level, 'level_type':level_type} 
    rows_df = pd.DataFrame(rows_dict)
    return rows_df

sheet_url = st.secrets["private_gsheets_url"]
rows = run_query(f'SELECT * FROM "{sheet_url}"')

st.dataframe(data=rows)



