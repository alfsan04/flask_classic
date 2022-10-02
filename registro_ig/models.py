from ast import Or
import sqlite3
from config import ORIGIN_DATA

def select_all():
    #creamos una conexión con la base de datos
    conn = sqlite3.connect(ORIGIN_DATA)
    #creamos el cursor
    cur = conn.cursor()
    #obtengo id, fecha, concepto y cantidad. No ponemos * por si la base de datos crece, así sólo importamos lo que nos interesa. No está bien visto poner asterisco
    result = cur.execute("SELECT id, date, concept, quantity from movements order by date;")

    filas = result.fetchall()
    columnas = result.description #no lleva paréntesis porque es un atributo de solo lectura, lo pone en la documentación
    
    #mezcla de filas y columnas para obtener lista de diccionarios
    resultado = []
    for fila in filas:
        d = {}
        for posicion, campo in enumerate(columnas):
            d[campo[0]] = fila[posicion]
        resultado.append(d)

    conn.close()

    return resultado

def insert(registro):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    #lo siguiente es comando de sql, decimos los títulos de las columnas (Date, concept, quantity) y luego los valores (?, ?, ?) que es obligado, por último lo que tiene que ir en esas interrogaciones
    cur.execute("INSERT INTO movements (date, concept, quantity) values (?, ?, ?);", registro)
    conn.commit()

    conn.close()

def select_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    result = cur.execute("SELECT id, date, concept, quantity from movements order by date;")

    filas = result.fetchall()
    columnas = result.description

    resultado = []
    for fila in filas:
        d = {}
        for posicion, campo in enumerate(columnas):
            d[campo[0]] = fila[posicion]
        resultado.append(d)

    conn.close()

    for diccionario in resultado:
        if diccionario["id"] == id:
            return diccionario

    return resultado

def updated_by(registro):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    #lo siguiente es comando de sql, decimos los títulos de las columnas (Date, concept, quantity) y luego los valores (?, ?, ?) que es obligado, por último lo que tiene que ir en esas interrogaciones
    lista = [registro[1],registro[2],registro[3],str(registro[0])]
    cur.execute("UPDATE movements SET date=?, concept=?, quantity=? where id=?", lista)
    conn.commit()

    conn.close()