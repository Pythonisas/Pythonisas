#!/usr/bin/python
# -*- coding: utf-8 -*-

import MySQLdb
import getpass
DB_PASS = getpass.getpass("Give me your MySQL password: ")
DB_HOST = 'localhost' 
DB_USER = 'root' 
DB_NAME = 'sqlexamples' 
 
def run_query(query=''): 
    datos = [DB_HOST, DB_USER, DB_PASS, DB_NAME] 
 
    conn = MySQLdb.connect(*datos) # Conectar a la base de datos 
    cursor = conn.cursor()         # Crear un cursor 
    cursor.execute(query)          # Ejecutar una consulta 
 
    if query.upper().startswith('SELECT'): 
        data = cursor.fetchall()   # Traer los resultados de un select 
    else: 
        conn.commit()              # Hacer efectiva la escritura de datos 
        data = None 
 
    cursor.close()                 # Cerrar el cursor 
    conn.close()                   # Cerrar la conexión 
 
    return data

#12.2.1.1. Insertar datos
dato1 = input("Entero: ")
dato2 = input("Otro entero: ")
#query = "INSERT INTO b (b2) VALUES ('%s')" % dato
query = "INSERT INTO b VALUES (1, 2)"
run_query(query)
query2 = "INSERT INTO b (b1, b2) VALUES ('%s', '%s')" % (dato1, dato2)
run_query(query2)
