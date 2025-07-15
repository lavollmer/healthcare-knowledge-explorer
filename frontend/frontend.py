import streamlit as st
import sqlite3

st.text('Healthcare Explorer')

conn = sqlite3.connect('../db/healthcare.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM healthcare_data LIMIT 10")
rows = cursor.fetchall()

col_names = [description[0] for description in cursor.description]

st.write("Data from healthcare database:")
st.table([dict(zip(col_names, row)) for row in rows])

conn.close()
    