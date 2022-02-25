# -*- coding: utf-8 -*-
"""
Created on Thu Feb 24 21:02:40 2022

@author: user

create table estadistica(
notas varchar(200),
media float(2),
mediana float(2),
moda float(2),
desviacion float(2),
varianza float(2),
fecha_operacion date)


"""
#%%
import numpy as np
import statistics
from statistics import mode
import psycopg2


#%%
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
    select = "select * from estadistica"
    cursor.execute(select)
    
    print("Resultado")
    tabla = cursor.fetchall()
    for registro in tabla:
        print("Notas = ", registro[0])
        print("Media = ", registro[1])
        print("Mediana = ", registro[2])
        print("Moda = ", registro[3])
        print("Desviación = ", registro[4])
        print("Varianza = ", registro[5])
        print("Fecha = ", registro[6], "\n")


#%%
print("Ingrese 5 notas de diferentes materias")
notas = []


for x in range(5):
    validacion = True
    while validacion == True:
        try:
            nota = int(input("ingrese la nota obtenida: "))
            notas.append(nota)
            validacion = False
        except:
            print("No se admite el valor")
            repetir = True
        

media = np.mean(notas)
mediana = np.median(notas)
moda = mode(notas)
desviacion = statistics.stdev(notas)
varianza = np.var(notas)


#%%
insert = "INSERT INTO estadistica VALUES('" + str(notas) + "', " + str(media) + ", " + str(mediana) + ", " + str(moda) + ", " + str(desviacion) + ", " + str(varianza) +  ", " + "NOW())"
cursor.execute(insert)
conexion.commit()

obtener = input("Ingrese el numero 1 si desea ver los datos completos: ")
if obtener == '1':
    select()
else:
    pass

