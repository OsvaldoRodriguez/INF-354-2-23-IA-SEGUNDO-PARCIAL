# SOLUCIÓN

### Dado el siguiente grafo:
### Generar el archivo CSV, obtener el mejor recorrido usando algoritmos genéticos sin el uso de DEAP.

![](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/grafo.PNG)


## 1. Explicación del Algoritmo genetico
* Se tiene las siguientes funciones
    * **Evaluación** .- la cual dado un camino encuentra el costo de dicho camino
    * **generar_poblacion**.- como es un grafo y los nodos son unicos se generar una matriz cada fila con una permutación aleatoria para simular un camino en el grafo
    * **cruce**.- se utiliza para crear nuevos individuos a partir de los padres
    * **mutacion**.- dado un camino se hace un cambio aleatorio entre dos nodos de dicho camino
    * **algoritmo genetico**.- calcula la mejor ruta para una cantidad determinada de generaciónes y poblacion
    * **Archivo csv**.- finalmente se guarda en un archivo .CSV

### 1.1 Código de la solución y Archivo .CSV
[Codigo (Python)](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/algoritmo_genetico_implementado_grafo.py)

[Archivo .CSV](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/mejor_recorrido_algoritmo_genetico_implementado.csv)

### 1.2 Ejecución

![](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/algoritmo_genetico_implementado_grafo.PNG)

## 2. Comprobación
* Se realizo un algoritmo básico de Backtraking para realizar todas las permutaciónes posibles y encontrar el mejor camino, dicha solución encuentra todos los caminos validos

[Codigo (Python)](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/algoritmo_del_grafo_fuerza_fruta.py)


[Archivo .CSV](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/mejor_recorrido_fuera_bruta.csv)

### 2.1 Ejecución

![](https://github.com/OsvaldoRodriguez/INF-354-2-23-IA-SEGUNDO-PARCIAL/blob/master/PREGUNTA%203/fuerza_bruta_todos_los_caminos.PNG)

