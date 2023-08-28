"""Escriba una función redondear()"""
import math
def redondear(n):
    e=math.trunc(n)
    if(n-e>=0.5):
        return e+1
    else:
        return e

n=float(input("Redondear: "))
print(redondear(n))



"""Coloque el módulo del ejercicio anterior dentro de un paquete"""
import redondear

n=float(input("Redondear: "))
print(redondear.redondear(n))



"""Usando el módulo datetime, escribe un programa que muestre la fecha
y hora actuales del sistema"""

from datetime import datetime

fec=datetime.now()
fecTexto=fec.strftime("%d/%m/%Y %H:%M")

print(fec)
print(fecTexto)



"""Bola mágica"""

import random

respuestas=["Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
pregunta=""
while True:
    pregunta=input("Escribe tu pregunta: ")
    if(pregunta=="salir"):
        break
    posi=random.randint(0,len(respuestas)-1)
    print(respuestas[posi])


"""Encuentre el tiempo de ejecución de los programas de los ejercicios
anteriores"""

import random,time

inicio=time.time()

respuestas=["Las chances son buenas","Puedes contar con ello","Pregúntame de nuevo más tarde","Concéntrate y pregunta de nuevo","No veo con claridad, intenta de nuevo","Mi respuesta es no","Mis fuentes me dicen que no"]
pregunta=""
while True:
    pregunta=input("Escribe tu pregunta: ")
    if(pregunta=="salir"):
        break
    posi=random.randint(0,len(respuestas)-1)
    print(respuestas[posi])

fin=time.time()
print("Has jugado durante "+str(fin-inicio)+" seg")



"""sorteo"""

import random,time

rifa=["Fefi","Julio","Chalup","Cami","Luna","Celina","Leito","Alejo"]

posicion=3
while posicion>0:
    sorteo=random.randint(0,len(rifa))
    print("El premio nro."+str(posicion)+" es para "+rifa[posicion])
    time.sleep(2)
    posicion-=1


""" Escriba una función que pida al usuario ingresar su fecha de
nacimiento"""
from  datetime import datetime

def dias():
    tucumple=input("ingrese su fecha de cumpleaños (d/m/a): ")
    hoy=datetime.today()
    fechaCumple=datetime.strptime(tucumple, '%d/%m/%Y')
    dias=hoy-fechaCumple
    print("ya tienes "+str(dias.days)+" dias ")

dias()




