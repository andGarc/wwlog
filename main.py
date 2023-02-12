# main.py

import streamlit as st
from deta import Deta

st.write("""
# Whitewater Log 🌊
""")

with st.form('log_form'):
    date = st.date_input('Date')

    river = st.selectbox(
        'Select a river section',
        ('Little Falls', 'Great Falls', 'Upper Yough')
    )

    level = st.number_input('Level', 
                        min_value=0.0, max_value=20000.0, step=0.01, value=3.0)

    level_type = st.radio(
                    'FT or CSF',
                    options=('FT', 'CFS')
                )

    notes = st.text_input('Notes', max_chars=200)

    # Every form must have a submit button.
    submitted = st.form_submit_button("Submit")

    # Connect to Deta Base with your Project Key
    deta = Deta(st.secrets['deta_key'])

    # Create a new database "wwlog-db"
    db = deta.Base("wwlog-db")

    # If the user clicked the submit button,
    # write the data from the form to the database.
    if submitted:
        st.markdown(f"""
            📝 **Entry**
            - Date: `{date}`
            - River: `{river}`
            - Level: `{level} {level_type}`
        """)
        db.put({'Date':date.strftime('%Y-%m-%d'), 'River': river,
                'Level':level, 'level_type':level_type, 'Notes':notes})

"---"
"Here's everything stored in the database:"
# This reads all items from the database and displays them to your app.
# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items
st.write(db_content)





