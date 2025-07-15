from db_config import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Patients (name, gender, birth_date) VALUES ('Alice Smith', 'F', '1990-05-12'), ('Bob Johnson', 'M', '1985-08-23'), ('Charlie Brown', 'M', '2000-01-15')")
    cursor.execute("INSERT INTO Conditions (condition_name) VALUES ('Hypertension'), ('Diabetes'), ('Asthma')")

    conn.commit()
    conn.close()