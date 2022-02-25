# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:20:30 2022

@author: user

create table numero_primo(
numero int,
resultado varchar(100),
fecha_operacion date)

"""

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
    select = "select * from numero_primo"
    cursor.execute(select)
    
    print("Resultado")
    tabla = cursor.fetchall()
    for registro in tabla:
        print("Numero = ", registro[0])
        print("Resultado = ", registro[1])
        print("Fecha = ", registro[2], "\n")

select()

#%%

validacion = True
while validacion == True:
    try:
        num = int(input("Ingrese un número: "))
        validacion = False
    except:
        print("No se admite el valor")


def es_primo(num):
    for n in range(2, num):
        if num % n == 0:
            return False
    return True



if es_primo(num) == True:
    resultado = "Es primo"
else:
    resultado = "Es compuesto"


#%%
insert = "INSERT INTO numero_primo VALUES(" + str(num) + ", '" + str(resultado) + "', " + "NOW())"
cursor.execute(insert)
conexion.commit()

obtener = input("Ingrese el numero 1 si desea ver los datos completos: ")
if obtener == '1':
    select()
else:
    pass
