import sqlite3
import os

# Ruta de la base de datos
DB_PATH = os.path.join(os.path.dirname(__file__), "historial.db")

def init_db():
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        """
        CREATE TABLE IF NOT EXISTS historial (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            prompt TEXT NOT NULL,
            respuesta TEXT NOT NULL,
            fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
        )
        """
    )
    conn.commit()
    conn.close()

def guardar_historial(prompt, respuesta):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO historial (prompt, respuesta) VALUES (?, ?)",
        (prompt, respuesta)
    )
    conn.commit()
    conn.close()

def obtener_historial(limit=5):
    conn = sqlite3.connect(DB_PATH)
    cursor = conn.cursor()
    cursor.execute(
        "SELECT prompt, respuesta FROM historial ORDER BY fecha DESC LIMIT ?", (limit,)
    )
    entries = cursor.fetchall()
    conn.close()
    return list(reversed(entries))
