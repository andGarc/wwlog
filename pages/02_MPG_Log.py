# /pages/log.py

import streamlit as st
import pandas as pd
import psycopg2
from db import add_record_mpg
from sqlalchemy import create_engine, text

st.write("""
# MPG Tracker
""")

with st.expander('Log a New Entry ✏️'):
    with st.form('log_form', clear_on_submit=True):

        actual_miles = st.number_input('Miles driven since last fill up', 
                            min_value=0.0, max_value=20000.0, step=0.01)

        date = st.date_input('Date')

        gallons = st.number_input('Gallons', 
                            min_value=0.0, max_value=20000.0, step=0.01)

        expected_miles = st.number_input('Expected Miles', 
                            min_value=0, max_value=800, step=1)


        # Every form must have a submit button.
        submitted = st.form_submit_button("Submit")


        # If the user clicked the submit button,
        # write the data from the form to the database.
        if submitted:
            st.markdown(f"""
                📝 **Entry**
                - Date: `{date}`
                - Gallons: `{gallons} gal`
                - Expected Miles: `{expected_miles} mi`
            """)
            # New record            
            data = {'Actual_Miles':[actual_miles],
                    'Date':[date.strftime('%Y-%m-%d')],
                    'Expected_Miles':[expected_miles],
                    'Gallons': [gallons]
                    }
            add_record_mpg(data)
            st.markdown('**Entry recorded.**')

"---"
st.write("""
## Entries
""")

# fetch all entries
db_url = st.secrets['db_url']
conn = psycopg2.connect(db_url)
engine = create_engine(db_url)
query = f"SELECT * FROM {st.secrets['mpg_table']}"
df = pd.read_sql_query(sql=text(query), con=engine.connect())
df = df.sort_values(by=['Date'], ascending=False)
df['MPG'] = round(df['Actual_Miles'] / df['Gallons'], 2)
st.dataframe(data=df[['Date','Actual_Miles','Expected_Miles',
                            'Gallons', 'MPG']])
conn.close()

# be able to edit an entry 