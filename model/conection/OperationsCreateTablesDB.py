from warnings import catch_warnings

from DatabaseConection import *




def createUsuarios():
    conn = getConecction()
    cursor = conn.cursor()
    try:
        cursor.execute("create table usuarios (dni text PRIMARY key, nombre text, apellidos text, edad int)")
    except DatabaseError as e:
        print("Ups, no se ha podido conectar con la base de datos " + str(e))
    finally:
        conn.close()
        cursor.close()


def createCoches():
    conn = getConecction()
    cursor = conn.cursor()
    try:
        cursor.execute("create table coches (matricula text, marca text, precio double, dni text, FOREIGN key (dni) references usuarios(dni)")
    except DatabaseError as e:
        print("Ups, no se ha podido conectar con la base de datos" + str(e))
    finally:
        conn.close()
        cursor.close()

def createMotos():
    conn = getConecction()
    cursor = conn.cursor()
    try:
        cursor.execute("create table motos (matricula text, marca text, precio double, dni text, FOREIGN key (dni) references usuarios(dni))")
    except DatabaseError as e:
        print("Ups, no se ha podido conectar con la base de datos" + str(e))
    conn.close()


def createBicicletas():
    try:
        cursor.execute("create table bicicletas (matricula text, marca text, precio double, dni text, FOREIGN key (dni) references usuarios(dni))")
    except DatabaseError as e:
        print("Ups, no se ha podido conectar con la base de datos" + str(e))


def dropTables():
    try:
        cursor.execute("drop table usuarios")
        cursor.execute("drop table coches")
        cursor.execute("drop table motos")
        cursor.execute("drop table bicicletas")
        conn.commit()
    except DatabaseError as e:
        print("Ups, no se han podido borrar las tablas " + str(e))
    finally:
        conn.close()
        cursor.close()






