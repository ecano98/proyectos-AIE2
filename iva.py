# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 22:09:46 2022

@author: user

create table iva(
precio float(2),
iva float(2),
precio_sin_iva float(2),
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
    select = "select * from iva"
    cursor.execute(select)
    
    print("Resultado")
    tabla = cursor.fetchall()
    for registro in tabla:
        print("Precio = ", registro[0])
        print("IVA = ", registro[1])
        print("Precio sin IVA = ", registro[2])
        print("Fecha = ", registro[3], "\n")


#%%
validacion = True

while validacion == True:
    try:
        precio = int(input("Ingrese el precio en quetzales: "))
        iva = precio*0.12
        precio_sin_iva = precio - precio*0.12
        validacion = False

    except:
        print("No se admite el valor")

insert = "INSERT INTO iva VALUES(" + str(precio) + ", " + str(iva) + ", " + str(precio_sin_iva) + ", " + "NOW())"
cursor.execute(insert)
conexion.commit()
validacion = False


obtener = input("Ingrese el numero 1 si desea ver los datos completos: ")
if obtener == '1':
    select()
else:
    pass


