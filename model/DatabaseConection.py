import sqlite3 as dbapi
from sqlite3 import DatabaseError, OperationalError


def getConecction():
    bbdd = dbapi.connect("alquiler.dat")
    return bbdd

getConecction()