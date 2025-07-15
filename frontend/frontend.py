import streamlit as st
import sqlite3

st.text('Healthcare Explorer Database Viewer: NOT real patient data, just a demo!')

conn = sqlite3.connect('../backend/healthcare.db')
cursor = conn.cursor()

query = """
    SELECT patient_id, name, gender, birth_date
    FROM Patients
    GROUP BY name, gender, birth_date
    LIMIT 10
"""

cursor.execute(query)
rows = cursor.fetchall()

col_names = [description[0] for description in cursor.description]

st.write("Data from healthcare database:")
st.table([dict(zip(col_names, row)) for row in rows])

conn.close()
    