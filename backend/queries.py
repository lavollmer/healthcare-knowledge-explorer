from db_config import get_connection


def query_common_treatments():
    conn = get_connection()
    df = pd.read_sql_query('''
            SELECT c.name AS condition, t.name AS treatment, COUNT(*) AS usage_count
            FROM Patient_Treatments pt
            JOIN Conditions c ON pt.condition_id = c.condition_id
            JOIN Treatments t ON pt.treatment_id = t.treatment_id
            GROUP BY c.name, t.name
            ORDER BY usage_count DESC;
                           ''', conn)
    
    print(df)
    conn.close()