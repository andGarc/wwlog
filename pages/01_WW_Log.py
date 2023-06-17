# main.py

import streamlit as st
from db import add_record_ww


st.set_page_config(
    page_title="AG Whitewater Log", layout="centered"
)

st.write("""
# AG Whitewater Log
""")

with st.form('log_form', clear_on_submit=True):
    date = st.date_input('Date')

    river = st.selectbox(
        'Select a river section',
        ('Little Falls', 'Great Falls', 'Yough', 'Other')
    )

    level = st.number_input('Level', 
                        min_value=0.0, max_value=20000.0, step=0.01)

    level_type = st.radio(
                    'FT or CSF',
                    options=('FT', 'CFS')
                )

    notes = st.text_input('Notes', max_chars=200)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    # If the user clicked the submit button,
    # write the data from the form to the database.
    if submitted:
        st.markdown(f"""
            📝 **Entry**
            - Date: `{date}`
            - River: `{river}`
            - Level: `{level} {level_type}`
        """)

        # New record            
        data = {'Date':[date],
                'Level':[level],
                'Notes': [notes],
                'River': [river],
                'level_type': [level_type]
                }
        add_record_ww(data)
        st.markdown('**Entry recorded.**')
