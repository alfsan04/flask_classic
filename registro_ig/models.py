from ast import Or
import sqlite3
from config import ORIGIN_DATA

def filas_to_diccionario(filas, columnas):
    resultado = []
    for fila in filas:
        d = {}
        for posicion, campo in enumerate(columnas):
            d[campo[0]] = fila[posicion]
        resultado.append(d)
    return resultado

def select_all():
    #creamos una conexión con la base de datos
    conn = sqlite3.connect(ORIGIN_DATA)
    #creamos el cursor
    cur = conn.cursor()
    #obtengo id, fecha, concepto y cantidad. No ponemos * por si la base de datos crece, así sólo importamos lo que nos interesa. No está bien visto poner asterisco
    cur.execute("SELECT id, date, concept, quantity from movements order by date;")

    resultado = filas_to_diccionario(cur.fetchall(), cur.description)

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
    cur.execute("SELECT id, date, concept, quantity FROM movements WHERE id = ?;", (id,)) #espera una tupla o lista, mejor una tupla que ocupa menos en memoria, (id,) convierte id en tupla

    resultado = filas_to_diccionario(cur.fetchall(), cur.description)

    conn.close()

    if resultado:
        return resultado[0] #el resultado es una lista con un único diccionario, que es lo que queremos, así que pasamos resultado[0] para que pase solo el diccionario y no la lista con el diccionario
    return {}

def updated_by(registro):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    #lo siguiente es comando de sql, decimos los títulos de las columnas (Date, concept, quantity) y luego los valores (?, ?, ?) que es obligado, por último lo que tiene que ir en esas interrogaciones
    lista = [registro[1],registro[2],registro[3],[registro[0]]]
    cur.execute("UPDATE movements SET date=?, concept=?, quantity=? where id=?", lista)
    conn.commit()

    conn.close()

def delete_by(id):
    conn = sqlite3.connect(ORIGIN_DATA)
    cur = conn.cursor()
    cur.execute("DELETE FROM movements WHERE id = ?", (id,))

    conn.commit()
    conn.close()