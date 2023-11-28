# -*- coding: utf-8 -*-
"""
Created on Wed Oct 25 11:29:13 2023

@author: AREA BASE DE DATOS
"""

import random

import numpy
import csv
from deap import algorithms
from deap import base
from deap import creator
from deap import tools
import pandas as pd
#Problem parameter
NB_AGENTE = 4
NB_QUEENS = 1  #agregando
#matriz=numpy.loadtxt("Agente1.csv",delimiter=";")
matriz = numpy.loadtxt("D:/OSVALDO/MI CARRERA/INFORMATICA/11 OPTATIVAS/INF 354 INTELIGENCIA ARTIFICIAL/II-2023/EXAMENES/SEGUNDO PARCIAL IA/PREGUNTA 4/grafito.csv", delimiter = ',')
NB_AGENTE = len(matriz)
print(matriz)
def evalAgente(individual):
    suma=0
    for i in range(len(individual)-1):
        suma=suma+matriz[individual[i],individual[i+1]]
    suma=suma+matriz[individual[len(individual)-1],individual[0]]  
    return suma,


creator.create("FitnessMin", base.Fitness, weights=(-1.0,))
creator.create("Individual", list, fitness=creator.FitnessMin)

#Since there is only one queen per line, 
#individual are represented by a permutation
toolbox = base.Toolbox()
toolbox.register("permutation", random.sample, range(NB_AGENTE), NB_AGENTE)

#Structure initializers
#An individual is a list that represents the position of each queen.
#Only the line is stored, the column is the index of the number in the list.
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.permutation)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evalAgente)
toolbox.register("mate", tools.cxPartialyMatched)
toolbox.register("mutate", tools.mutShuffleIndexes, indpb=2.0/NB_QUEENS)
toolbox.register("select", tools.selTournament, tournsize=3)

def main(seed = 0):
    random.seed(seed)
    pop = toolbox.population(n=100)
    hof = tools.HallOfFame(1)
    stats = tools.Statistics(lambda ind: ind.fitness.values)
    stats.register("Avg", numpy.mean)
    stats.register("Std", numpy.std)
    stats.register("Min", numpy.min)
    stats.register("Max", numpy.max)

    algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen=100, stats=stats,
                        halloffame=hof, verbose=True)

    return pop, stats, hof

if __name__ == "__main__":
    pop, stats, hof = main()
    print(matriz)
    print("Minima Distancia", evalAgente(hof[0]))
    print("Mejor Camino", hof)
    nombre_archivo = 'mejor_recorrido_algoritmo_genetico_deap.csv'
    
    with open(nombre_archivo, mode='w', newline='') as archivo_csv:
        escritor_csv = csv.writer(archivo_csv)
        escritor_csv.writerows(hof)
        escritor_csv.writerow(['Distancia mas corta es: ' + str(evalAgente(hof[0]))])
