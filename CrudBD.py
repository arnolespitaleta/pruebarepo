import psycopg2

# Conecta a la base de datos
conn = psycopg2.connect(
    host="localhost",
    database="ejemplo",
    user="postgres",
    password="12345678"
)

# Crea una tabla en la base de datos
cur = conn.cursor()
cur.execute("""
    CREATE TABLE usuarios (
        id SERIAL PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(50)
    )
""")
conn.commit()

# Crea un registro en la tabla
cur = conn.cursor()
cur.execute("""
    INSERT INTO usuarios (name, email)
    VALUES ('John Doe', 'john.doe@example.com')
""")
conn.commit()

# Lee un registro de la tabla
cur = conn.cursor()
cur.execute("""
    SELECT * FROM usuarios WHERE id = 1
""")
row = cur.fetchone()
print(row)

# Actualiza un registro en la tabla
cur = conn.cursor()
cur.execute("""
    UPDATE usuarios SET email = 'johndoe@example.com' WHERE id = 1
""")
conn.commit()

# Elimina un registro de la tabla
cur = conn.cursor()
cur.execute("""
    DELETE FROM usuarios WHERE id = 1
""")
conn.commit()

# Cierra la conexión a la base de datos
cur.close()
conn.close()
