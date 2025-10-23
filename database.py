"""Simple SQLite wrapper for storing documents and extracted entities."""
import sqlite3
import json
from typing import Dict, Any, List

DB_PATH = 'data/intelligent_workflow.db'

def init_db(path: str = DB_PATH):
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('''
        CREATE TABLE IF NOT EXISTS documents (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            text TEXT,
            entities TEXT
        )
    ''')
    conn.commit()
    conn.close()

def save_document(text: str, entities: Dict[str, Any], path: str = DB_PATH) -> int:
    init_db(path)
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('INSERT INTO documents (text, entities) VALUES (?, ?)', (text, json.dumps(entities)))
    doc_id = cur.lastrowid
    conn.commit()
    conn.close()
    return doc_id

def get_documents(path: str = DB_PATH) -> List[Dict[str, Any]]:
    init_db(path)
    conn = sqlite3.connect(path)
    cur = conn.cursor()
    cur.execute('SELECT id, text, entities FROM documents')
    rows = cur.fetchall()
    conn.close()
    return [{'id': r[0], 'text': r[1], 'entities': json.loads(r[2]) if r[2] else {}} for r in rows]
