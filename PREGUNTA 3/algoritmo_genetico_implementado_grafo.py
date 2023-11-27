# -*- coding: utf-8 -*-
"""
Created on Mon Nov 27 18:27:01 2023

@author: Fury
"""

import random
import numpy
import csv

# Función para calcular la distancia total de un recorrido
def evaluacion(camino, grafo):
    ans = 0
    for i in range(len(camino) - 1):
        ans += grafo[camino[i]][camino[i + 1]]
    ans += grafo[camino[-1]][camino[0]]  # Volver a la ciudad de inicio
    return ans

# Función para generar una población inicial de recorridos aleatorios
def generar_poblacion(tam_poblacion, cantidad_ciudades):
    poblacion = []
    for _ in range(tam_poblacion):
        camino = list(range(cantidad_ciudades))
        random.shuffle(camino)
        poblacion.append(camino)
    return poblacion

# Función de cruce (cruce) para crear nuevos individuos a partir de dos padres
def cruce(padre1, padre2):
    punto_corte = random.randint(0, len(padre1) - 1)
    hijo = padre1[:punto_corte] + [ciudad for ciudad in padre2 if ciudad not in padre1[:punto_corte]]
    return hijo

# Función de mutación para introducir pequeños cambios en un individuo
def mutacion(recorrido):
    indice1, indice2 = random.sample(range(len(recorrido)), 2)
    recorrido[indice1], recorrido[indice2] = recorrido[indice2], recorrido[indice1]

# Función principal del algoritmo genético
def algoritmo_genetico(num_generaciones, tamano_poblacion, distancias):
    num_ciudades = len(distancias)
    # se esta generando la polacion de manera aleatoria
    poblacion = generar_poblacion(tamano_poblacion, num_ciudades)
    for generacion in range(num_generaciones):
        poblacion = sorted(poblacion, key=lambda x: evaluacion(x, distancias))
        # Seleccionar los mejores individuos (padres)
        padres = poblacion[:tamano_poblacion // 2]

        # Crear nuevos individuos (hijos) mediante cruce y mutación
        hijos = []
        for _ in range(tamano_poblacion // 2):
            padre1 = random.choice(padres)
            padre2 = random.choice(padres)
            hijo = cruce(padre1, padre2)
            mutacion(hijo)
            hijos.append(hijo)

        # Reemplazar la población anterior con la nueva generada
        poblacion = padres + hijos

    mejor_recorrido = poblacion[0]
    mejor_distancia = evaluacion(mejor_recorrido, distancias)
    return mejor_recorrido, mejor_distancia

# Ejemplo de uso
# Definir distancias entre ciudades (puedes ajustar esto según tu problema)
distancias_entre_ciudades = numpy.loadtxt("D:/OSVALDO/MI CARRERA/INFORMATICA/11 OPTATIVAS/INF 354 INTELIGENCIA ARTIFICIAL/II-2023/EXAMENES/SEGUNDO PARCIAL IA/PREGUNTA 4/grafito.csv", delimiter = ',')
print(distancias_entre_ciudades)

num_generaciones = 100
tamano_poblacion = 50

mejor_recorrido, mejor_distancia = algoritmo_genetico(num_generaciones, tamano_poblacion, distancias_entre_ciudades)

# Guardar el resultado en un archivo CSV
with open('mejor_recorrido.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Ciudad'])
    for ciudad in mejor_recorrido:
        writer.writerow([ciudad])
    writer.writerow(['Distancia mas corta es: ' + str(mejor_distancia)])

print(f"Mejor recorrido encontrado: {mejor_recorrido}")
print(f"Distancia total: {mejor_distancia}")
