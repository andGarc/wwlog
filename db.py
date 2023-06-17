import psycopg2
import streamlit as st
import pandas as pd
from sqlalchemy import create_engine, text

def add_record_ww(record):
    df = pd.DataFrame(record)
    db_url = st.secrets['db_url']
    table =  st.secrets['ww_table']
    conn = psycopg2.connect(db_url)
    engine = create_engine(db_url)
    df.to_sql(table, engine, if_exists='append', index=False)

def add_record_mpg(record):
    df = pd.DataFrame(record)
    db_url = st.secrets['db_url']
    table =  st.secrets['mpg_table']
    conn = psycopg2.connect(db_url)
    engine = create_engine(db_url)
    df.to_sql(table, engine, if_exists='append', index=False)

    # update last record
    # Create a cursor object to interact with the database
    cursor = conn.cursor()

    # update actual miles for last record
    update_query = f"""
        UPDATE {table}
        SET "Actual_Miles" = {record['Actual_Miles'][0]}
        WHERE "Actual_Miles" = 0
    """
    cursor.execute(update_query)
    conn.commit()
    cursor.close()

    conn.close()