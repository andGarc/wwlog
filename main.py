# main.py

import streamlit as st
import pandas as pd
from deta import Deta
from streamlit_elements import elements, mui, html
from streamlit_elements import nivo

st.write("""
# Whitewater Log
""")

# Connect to Deta Base with your Project Key
deta = Deta(st.secrets['deta_key'])

# Create a new database "wwlog-db"
db = deta.Base("wwlog-db")

# db_content is a list of dictionaries. You can do everything you want with it.
db_content = db.fetch().items

"---"
st.markdown(f"**{len(db_content)}** session so far in 2023.")
#############
# process db_contene
# turn to df
df_content = pd.DataFrame(db_content)
#############
# get lastest entry
last_time = df_content.sort_values(by=['Date']).iloc[-1]['Date']
st.markdown(f"You were last on the river on **{last_time}**.")
#############

# get month of date column
df_content['Month_Year'] = df_content['Date'].apply(lambda x: x[:7]) 

# get counts per month/year
df_river_count = df_content.groupby(['Month_Year'])['key'].count().to_frame().reset_index()
# turn each row to a dic
data_dic = df_river_count.to_dict(orient='records')


"---"
st.markdown("##### Monthly Summary")
with elements("nivo_charts"):
    DATA = data_dic

    with mui.Box(sx={"height": 500}):
        nivo.Bar(
            data=DATA,
            keys=["key"],
            indexBy="Month_Year",
            valueFormat="0",
            margin={ "top": 70, "right": 80, "bottom": 40, "left": 80 },
            borderColor={ "from": "color" },
            gridLabelOffset=36,
            dotSize=10,
            dotColor={ "theme": "background" },
            dotBorderWidth=2,
            motionConfig="wobbly",
            theme={
                "background": "#FFFFFF",
                "textColor": "#31333F",
            }
        )