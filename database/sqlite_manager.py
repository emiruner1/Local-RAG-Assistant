import sqlite3
from config import DATABASE


def get_connection():
    return sqlite3.connect(DATABASE)


def create_table():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS documents(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        source TEXT,
        content TEXT,
        embedding TEXT
    )
    """)

    conn.commit()
    conn.close()


def insert_chunk(source, content, embedding):
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute(
        "INSERT INTO documents(source, content, embedding) VALUES(?,?,?)",
        (source, content, embedding)
    )

    conn.commit()
    conn.close()


def get_all_chunks():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT source, content, embedding FROM documents")

    rows = cursor.fetchall()

    conn.close()

    return rows


def document_list():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT DISTINCT source FROM documents")

    rows = cursor.fetchall()

    conn.close()

    return [row[0] for row in rows]


def chunk_count():
    conn = get_connection()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM documents")

    count = cursor.fetchone()[0]

    conn.close()

    return count


def delete_database():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM documents")
    conn.commit()
    conn.close()
