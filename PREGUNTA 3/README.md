# SOLUCIÓN

### Dado el siguiente grafo:
### Generar el archivo CSV, obtener el mejor recorrido usando algoritmos genéticos sin el uso de DEAP.

![]()


## 1. Explicación del Algoritmo genetico
* Se tiene las siguientes funciones
    * **Evaluación** .- la cual dado un camino encuentra el costo de dicho camino
    * **generar_poblacion**.- como es un grafo y los nodos son unicos se generar una matriz cada fila con una permutación aleatoria para simular un camino en el grafo
    * **cruce**.- se utiliza para crear nuevos individuos a partir de los padres
    * **mutacion**.- dado un camino se hace un cambio aleatorio entre dos nodos de dicho camino
    * **algoritmo genetico**.- calcula la mejor ruta para una cantidad determinada de generaciónes y poblacion
    * **Archivo csv**.- finalmente se guarda en un archivo .CSV

### 1.1 Código de la solución y Archivo .CSV
![Codigo (Python)]()

![Archivo .CSV]()

### 1.2 Ejecución


## 2. Comprobación
* Se realizo un algoritmo básico de Backtraking para realizar todas las permutaciónes posibles y encontrar el mejor camino, dicha solución encuentra todos los caminos validos

![Codigo (Python)]()

![Archivo .CSV]()

### 2.1 Ejecución

