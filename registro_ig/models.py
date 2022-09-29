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