from DatabaseConection import *

def create_table(query):
    conn = getConecction()
    cursor = conn.cursor()
    try:
        cursor.execute(query)
        conn.commit()
    except Exception as e:
        print("Ups, no se ha podido conectar con la base de datos: " + str(e))
        conn.rollback()
    finally:
        cursor.close()
        conn.close()

def createUsuarios():
    return "CREATE TABLE usuarios (dni TEXT PRIMARY KEY not null, nombre TEXT, apellidos TEXT, edad INT)"

def createCoches():
    return "CREATE TABLE coches (matricula TEXT PRIMARY key not null, marca TEXT, precio REAL, dni TEXT, FOREIGN KEY (dni) REFERENCES usuarios(dni))"

def createMotos():
    return "CREATE TABLE motos (matricula TEXT PRIMARY key not null, marca TEXT, precio REAL, dni TEXT, FOREIGN KEY (dni) REFERENCES usuarios(dni))"

def createBicicletas():
    return "CREATE TABLE bicicletas (matricula TEXT PRIMARY key not null, marca TEXT, precio REAL, dni TEXT, FOREIGN KEY (dni) REFERENCES usuarios(dni))"

def dropTables():
    conn = getConecction()
    cursor = conn.cursor()
    try:
        cursor.execute("DROP TABLE IF EXISTS usuarios")
        cursor.execute("DROP TABLE IF EXISTS coches")
        cursor.execute("DROP TABLE IF EXISTS motos")
        cursor.execute("DROP TABLE IF EXISTS bicicletas")
        conn.commit()
    except Exception as e:
        print("Ups, no se han podido borrar las tablas: " + str(e))
        conn.rollback()
    finally:
        cursor.close()
        conn.close()