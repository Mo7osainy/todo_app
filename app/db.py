import psycopg2
import os

DB_PARAMS = {
    "dbname": os.getenv("POSTGRES_DB", "todo_db"),
    "user": os.getenv("POSTGRES_USER", "todo_user"),
    "password": os.getenv("POSTGRES_PASSWORD", "todo_pass"),
    "host": os.getenv("DB_HOST", "db"),
    "port": 5432
}

def get_db():
    return psycopg2.connect(**DB_PARAMS)

def init_db():
    conn = get_db()
    cur = conn.cursor()
    cur.execute("""
        CREATE TABLE IF NOT EXISTS tasks (
            id SERIAL PRIMARY KEY,
            title TEXT NOT NULL
        );
    """)
    conn.commit()
    cur.close()
    conn.close()
