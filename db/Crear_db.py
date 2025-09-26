import sqlite3
import os

# Esto se asegura que la carpeta 'db/' exista
if not os.path.exists('db'):
    os.makedirs('db')

# Ruta a la base de datos
db_path = os.path.join('db', 'usuarios.db')

# Conexión a la base de datos
conn = sqlite3.connect(db_path)
cursor = conn.cursor()

# Tabla de usuarios
cursor.execute('''
    CREATE TABLE IF NOT EXISTS usuarios (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        email TEXT NOT NULL UNIQUE,
        password TEXT NOT NULL
    )
''')

# Guardar cambios y cerrar
conn.commit()
conn.close()


