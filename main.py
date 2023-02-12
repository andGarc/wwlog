import streamlit as st

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
    if submitted:
        st.markdown(f"""
            📝 **Entry**
            - Date: `{date}`
            - River: `{river}`
            - Level: `{level} {level_type}`
        """)
