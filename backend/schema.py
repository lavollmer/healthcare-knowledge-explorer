# Database schema using sqlite3 built into Python

from db_config import get_connection

def create_table():
    conn = get_connection()
    # Cursor object to execute SQL commands
    cursor = conn.cursor()

    cursor.executescript('''
    CREATE TABLE IF NOT EXISTS Patients (
        patient_id INTEGER PRIMARY KEY,
        name TEXT,
        gender TEXT,
        birth_date DATE
    );

    CREATE TABLE IF NOT EXISTS Conditions (
        condition_id INTEGER PRIMARY KEY,
        name TEXT
    );
                
    CREATE TABLE IF NOT EXISTS Medications (
        medication_id INTEGER PRIMARY KEY,
        brand_name TEXT,
        generic_name TEXT,
        dosage_form TEXT
    );

        ''')

    conn.commit()
    conn.close()

