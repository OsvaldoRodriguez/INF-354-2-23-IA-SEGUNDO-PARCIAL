# SOLUCIÓN

### Dado la función $f(x)=x^3+1$ en excel realice al menos tres generaciones del funcionamiento del algoritmo genético.

* Se simulo el proceso utilizando con la cada individuo de la población de la siguiente manera
    > se ordena la población de manera decreciente
    > Se obtiene el binario de cada individuo
    > Para el cruce se intercambia los 3 ultimos bits de cada numero entre dos consecutivos
    > para la Mutación solo se aplica XOR al bit en la posicion 4 (izq a der index 1)
    > se simula 3 generaciones del mismo

