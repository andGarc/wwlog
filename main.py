# main.py

import altair as alt
import streamlit as st
import pandas as pd
from deta import Deta
from streamlit_elements import elements, mui
from streamlit_elements import nivo


st.set_page_config(
    page_title="AG Whitewater Log", layout="centered"
)

# get data
def get_data():
    # Connect to Deta Base with your Project Key and fetch items
    deta = Deta(st.secrets['deta_key'])
    db = deta.Base("wwlog-db")
    data = db.fetch().items
    data =  pd.DataFrame(data)
    # get month and year into a column
    data['Month_Year'] = data['Date'].apply(lambda x: x[:7]) 
    return data

# get number of sessions 
def get_total_sessions(df):
    return len(df)

# get latest session
def get_lastest_session(df):
    last_time = df.sort_values(by=['Date']).iloc[-1]['Date']
    return last_time

# bar chart 
def get_trend_bar_chart(df):
    # group and select records for the latest month
    data = df.groupby(['Month_Year'])['key'].count().to_frame().reset_index()

    # make chart
    bar_chart = alt.Chart(data).mark_bar().encode(
        x=alt.X('Month_Year', axis=alt.Axis(title='')),
        y=alt.Y('key', axis=alt.Axis(title='# sessions')),
        color=alt.value('grey')
    ).interactive()

    # add labels to the bars
    text = alt.Chart(data).mark_text(
        align='center',
        baseline='middle',
        dy=-5  # Adjust the vertical position of the labels
    ).encode(
        x='Month_Year',
        y='key',
        text='key:Q'
    )

    bar_chart_with_labels = bar_chart + text

    return bar_chart_with_labels

# donut chart
def get_donut_chart(df):
    # get max date data
    max_date = df['Month_Year'].max()
    # group and select records for the latest month
    data = df.groupby(['Month_Year', 'River'])['key'].count().to_frame().reset_index()
    max_date_records = data[data['Month_Year'] == max_date]
    # make chart
    donut_chart = alt.Chart(max_date_records).mark_arc(innerRadius=80).encode(
        theta="key",
        color="River:N",
    ).interactive()
    return donut_chart


source_data = get_data()

st.write("""
# AG Whitewater Log
""")      
"---"
st.markdown(f"**{get_total_sessions(source_data)}** sessions in 2023.")
st.markdown(f"You were last on the river on **{get_lastest_session(source_data)}**.")

# get counts per month/year
df_river_count = source_data.groupby(['Month_Year',])['key'].count().to_frame().reset_index()
# turn each row to a dic
data_dic = df_river_count.to_dict(orient='records')

"---"
st.markdown("##### Current Month")
st.altair_chart(get_donut_chart(source_data), use_container_width=True)

"---"
st.markdown("##### Monthly Trend")
st.altair_chart(get_trend_bar_chart(source_data), use_container_width=True)
