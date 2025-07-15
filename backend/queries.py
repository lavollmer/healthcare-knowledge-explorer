from db_config import get_connection

def query_common_treatments():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute('''
    SELECT c.name AS condition, t.name AS treatment, COUNT(*) AS usage_count
    FROM Patient_Treatments pt
    JOIN Conditions c ON pt.condition_id = c.condition_id
    JOIN Treatments t ON pt.treatment_id = t.treatment_id
    GROUP BY c.name, t.name
    ORDER BY usage_count DESC;
    ''', conn)

    rows = cursor.fetchall()

    print(f"{'Condition':<20} {'Treatment':<20}{'Usage Count':<12}")
    print("-" * 54)

    for condition,treatment,usage_count in rows:
        print(f"{condition:<20} {treatment:<20} {usage_count:<20}")
        
    conn.close()