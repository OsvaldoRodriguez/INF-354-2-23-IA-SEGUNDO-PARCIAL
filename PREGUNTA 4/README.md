# SOLUCIÓN

### Dado el siguiente grafo:
### Generar el archivo CSV, obtener el mejor recorrido usando algoritmos genéticos sin el uso de DEAP.

![](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/grafo.PNG)


## 1. Explicación del Algoritmo genetico usando Deap
* Se tiene las siguientes funciones
    * **evalAgente** .- la cual dado un camino encuentra el costo de dicho camino
Las demas funciones son propias de Deap para algoritmos geneticos

### 1.1 Código de la solución y Archivo .CSV
[Codigo (Python)](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/queens.py)

[Archivo .CSV](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/mejor_recorrido_algoritmo_genetico_deap.csv)

### 1.2 Ejecución

![](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/mejor_recorrido_algoritmo_genetico_deap.PNG)

## 2. Comprobación
* Se realizo un algoritmo básico de Backtraking para realizar todas las permutaciónes posibles y encontrar el mejor camino, dicha solución encuentra todos los caminos validos

[Codigo (Python)](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/algoritmo_del_grafo_fuerza_fruta.py)


[Archivo .CSV](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/mejor_recorrido_fuera_bruta.csv)

### 2.1 Ejecución

![](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%204/fuerza_bruta_todos_los_caminos.PNG)

