# -*- coding: utf-8 -*-
"""

@author: ecano 201700416
"""

"""
create table juego_gran8(
primer_dado int,
segundo_dado int,
total_dado int,
resultado varchar(50),
fecha_operacion date)

"""


#%%
import random
import psycopg2


try:
    conexion = psycopg2.connect(
        host = "localhost",
        port = "5432",
        user = "postgres",
        password = "Tlpecqmff.",
        dbname = "proyectos_usac"
    )
    print("Conexión exitosa")
except:
    print("Ocurrió un error en la conexión, verifique los parámetros")
cursor = conexion.cursor()

#%%

def select():
    select = "select * from juego_gran8"
    cursor.execute(select)
    
    print("Resultado")
    tabla = cursor.fetchall()
    for registro in tabla:
        print("Primer dado = ", registro[0])
        print("Segundo dado = ", registro[1])
        print("Total dados = ", registro[2])
        print("Resultado = ", registro[3])
        print("Fecha = ", registro[4], "\n")
          

#%%

valor = True
while valor == True:
    
    input("Presiona Enter para lanzar el primer dado... ")
    x = random.randint(1,6)
    print("Dado 1: " + str(x))
    
    input("Presiona Enter para lanzar el segundo dado... ")
    y = random.randint(1,6)
    print("Dado 2: " + str(y))
    
    input("Presiona Enter para ver el resultado... ") 
    z = x + y
    print("Total: " + str(z))
    
    if z == 8:
        resultado = "Ganaste"
        print(resultado)
        valor = False
        
    elif z == 7:
        resultado = "Perdiste"
        print(resultado)
        valor = False
    
    else:
        resultado = "Vuelve a intentarlo"
        print(resultado)
    
    insert = "INSERT INTO juego_gran8 VALUES(" + str(x) + ", " + str(y) + ", " + str(z) + ", " + "'" + resultado +"' " + ", " + "NOW())"
    cursor.execute(insert)
    conexion.commit()
    
obtener = input("Ingrese el numero 1 si desea ver los datos completos: ")
if obtener == '1':
    select()
else:
    pass