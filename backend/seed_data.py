from db_config import get_connection

def seed_data():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO Patients VALUES (1, 'Alice Smith', 'F', '1990-05-12')")
    cursor.execute("INSERT INTO Conditions VALUES (1,'Hypertension')")

    conn.commit()
    conn.close()