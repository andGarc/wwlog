import psycopg2
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

def add_record_ww(record):
    df = pd.DataFrame(record)
    db_url = st.secrets['db_url']
    table =  st.secrets['ww_table']
    conn = psycopg2.connect(db_url)
    print(db_url)
    engine = create_engine(db_url)
    df.to_sql(table, engine, if_exists='append', index=False)

def get_total_sessions_ww():
    db_url = st.secrets['db_url']
    table =  st.secrets['ww_table']
    conn = psycopg2.connect(db_url)
    engine = create_engine(db_url)
    query = f"SELECT COUNT(*) FROM {table}"
    count_df = pd.read_sql_query(text(query), engine.connect())
    return count_df.iloc[0][0]

def get_last_on_river_ww():
    db_url = st.secrets['db_url']
    table =  st.secrets['ww_table']
    conn = psycopg2.connect(db_url)
    engine = create_engine(db_url)
    query = f'SELECT MAX("Date") FROM {table}'
    date_df = pd.read_sql_query(text(query), engine.connect())
    return date_df.iloc[0][0]