# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 11:47:42 2023
@author: Fury
"""
import random 
import numpy
import csv
PATH = []

MIN_PATH = 10**19
def calculatePath(individuo):
    nuevo = individuo.copy()
    nuevo.append(nuevo[0])
    #print(nuevo)
    path = 0
    for i in range(1, len(nuevo)):
        path += matriz[nuevo[i - 1]][nuevo[i]]
    
    return path
def permutation(paths):
    global MIN_PATH
    if(len(paths) == NB_AGENT):
        cur = calculatePath(paths)
        print(paths, cur)
        if MIN_PATH > cur:
            MIN_PATH = cur
            PATH.clear()
            
            nuevo_camino = []
            for i in paths:
                nuevo_camino.append(i)
            PATH.append(nuevo_camino)
        elif MIN_PATH == cur:
            
            nuevo_camino = []
            for i in paths:
                nuevo_camino.append(i)
            PATH.append(nuevo_camino)

    else:
        for i in range(NB_AGENT):
            if used[i] == 0:
                used[i] = 1
                paths.append(i)
                permutation(paths)
                paths.pop()
                used[i] = 0
            



matriz = numpy.loadtxt("D:/OSVALDO/MI CARRERA/INFORMATICA/11 OPTATIVAS/INF 354 INTELIGENCIA ARTIFICIAL/II-2023/EXAMENES/SEGUNDO PARCIAL IA/PREGUNTA 4/grafito.csv", delimiter = ',')
NB_AGENT = len(matriz[0])
used  = [0] * NB_AGENT
paths = []

print(matriz)

# add node to comeback where started it
#print(individuo)

permutation(paths)

print("COSTO MINIMO", MIN_PATH)
print("caminos")
for i in PATH:
    print(i)
    
nombre_archivo = 'mejor_recorrido_fuera_bruta.csv'

with open(nombre_archivo, mode='w', newline='') as archivo_csv:
    escritor_csv = csv.writer(archivo_csv)
    escritor_csv.writerows(PATH)
    escritor_csv.writerow(['Distancia mas corta es: ' + str(MIN_PATH)])
