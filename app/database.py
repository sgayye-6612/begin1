import psycopg2
try:
    conn = psycopg2.connect(
        host="localhost",
        database="ecomm_db",
        user="postgres",
        password="1234",
        port="5432"
    )
    cursor = conn.cursor()

    print("Connected to PostgreSQL Successfully!")
except Exception as e:
    print("Connection Error:", e)
