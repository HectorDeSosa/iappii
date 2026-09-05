import sqlite3


def conectar():
    return sqlite3.connect("productos.db")


def crear_tabla():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS productos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nombre TEXT NOT NULL,
            categoria TEXT NOT NULL,
            precio REAL NOT NULL,
            stock INTEGER NOT NULL
        )
    """)

    conexion.commit()
    conexion.close()


def cargar_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    productos = [
        ("Notebook Lenovo IdeaPad", "Notebook", 850000, 5),
        ("Mouse Logitech M185", "Mouse", 15000, 20),
        ("Teclado Redragon Kumara", "Teclado", 45000, 10),
        ("Monitor Samsung 24 pulgadas", "Monitor", 220000, 7),
        ("Auriculares HyperX Cloud", "Auriculares", 95000, 4)
    ]

    cursor.executemany("""
        INSERT INTO productos (nombre, categoria, precio, stock)
        VALUES (?, ?, ?, ?)
    """, productos)

    conexion.commit()
    conexion.close()


def obtener_productos():
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, categoria, precio, stock
        FROM productos
    """)

    productos = cursor.fetchall()

    conexion.close()

    return productos

def buscar_productos(consulta):
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("""
        SELECT id, nombre, categoria, precio, stock
        FROM productos
        WHERE nombre LIKE ? OR categoria LIKE ?
    """, (f"%{consulta}%", f"%{consulta}%"))

    productos = cursor.fetchall()

    conexion.close()

    return productos

if __name__ == "__main__":
    crear_tabla()

    # Solo cargar los productos si la tabla está vacía
    conexion = conectar()
    cursor = conexion.cursor()

    cursor.execute("SELECT COUNT(*) FROM productos")
    cantidad = cursor.fetchone()[0]

    conexion.close()

    if cantidad == 0:
        cargar_productos()
        print("Base de datos creada y productos cargados.")
    else:
        print("La base de datos ya contiene productos.")