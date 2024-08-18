import psycopg2
import streamlit as st
import pandas as pd
from datetime import datetime
from sqlalchemy import create_engine, text

def add_record_ww(record):
    df = pd.DataFrame(record)
    db_url = st.secrets['db_url']
    table =  st.secrets['ww_table']
    conn = psycopg2.connect(db_url)
    print(db_url)
    engine = create_engine(db_url)
    df.to_sql(table, engine, if_exists='append', index=False)

@st.cache_data
def load_data():
    db_url = st.secrets['db_url']
    table =  st.secrets['ww_table']
    conn = psycopg2.connect(db_url)
    engine = create_engine(db_url)
    query = f"SELECT * FROM {table}"
    df = pd.read_sql_query(text(query), engine.connect())
    df['Date'] = pd.to_datetime(df['Date'])
    return df

def get_total_sessions_ww_curr_year(df, year=datetime.now().year):
    # extract the year from the date column
    df['year'] = df['Date'].dt.year
    # group by year an get the count
    year_counts = df.groupby('year').size().reset_index(name='count')
    # return the value for the latest year
    return year_counts[year_counts['year'] == year]['count'].iloc[0]

def get_last_on_river_ww(df):
    return df['Date'].dt.date.max()