import streamlit as st
import sqlite3

st.text('Healthcare Explorer Database Viewer: NOT real patient data, just a demo!')

conn = sqlite3.connect('../backend/healthcare.db')
cursor = conn.cursor()

cursor.execute("SELECT * FROM Patients LIMIT 10")
rows = cursor.fetchall()

col_names = [description[0] for description in cursor.description]

st.write("Data from healthcare database:")
st.table([dict(zip(col_names, row)) for row in rows])

conn.close()
    