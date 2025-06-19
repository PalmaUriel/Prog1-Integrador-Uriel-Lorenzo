import time
import random

### Generación de listas de tamaños crecientes con números aleatorios

numeros_0 = [random.randint(1, 1000000) for i in range(1000)]                    ###Se generan listas que crecen desde los Mil, 10mil, 100mil, 1 millón y 10 millones
numeros_1 = [random.randint(1, 1000000) for i in range(10000)]                   ###Cada número es un entero aleatorio entre 1 y 1.000.000
numeros_2 = [random.randint(1, 1000000) for i in range(100000)]
numeros_3 = [random.randint(1, 1000000) for i in range(1000000)]
numeros_4 = [random.randint(1, 1000000) for i in range(10000000)]
numeros_total = [numeros_0, numeros_1, numeros_2, numeros_3, numeros_4]           ###Se guardan todas las listas dentro de otra lista para un facil procesamiento

### Definición de Funciones

def min_manual(lista):                                  #Encuentra el valor mínimo de la lista de forma manual(Sin usar min(). Tiene complejidad: O(n).
    if not lista:                           ### 1
        return None                                     #Si la lista esta vacía retorna un "None"
    minimo = lista[0]                       ### 1       #Se asume que el primer número será el menor
    for numero in lista:                    ### 2n     T(n) = 1 + 1 + 2n + 1 = 2n + 3 == O(n)
        if numero < minimo:                 ### 1
            minimo = numero                 ### 1
    return minimo                           ### 1

def min_auto(lista):                                    #Encuentra el valor mínimo de la lista usando la función min() ya definida en Python. Tiene complejidad: O(n).
    if not lista:                           ### 1
        return None                         ### 1       T(n) = 1 + 1 + n = n + 2 == O(n)
    return min(lista)                       ### n       #Función con una optimización interna.

print("Resultados de la búsqueda del minimo automático")        #Resultados con la función min() (Automática)

###Se recorre cada lista y se mide el tiempo que tarda "min_auto" en encontrar el número menor
for i in range(5):
    inicio = time.time()                        #Se guarda el tiempo de inicio
    minimo_auto = min_auto(numeros_total[i])    #Se ejecuta la función automatica
    tiempo = time.time() - inicio               #Se realiza el calculo para ver el tiempo transcurrido
    print(f"{10**(i+3)} {tiempo:.10f}")

print("Resultados de la búsqueda del minimo manual")            #Resultados con la función manual

###Se recorre cada lista y se mide el tiempo que tarda "min_manual" en encontrar el número menor
for i in range(5):
    inicio = time.time()                            #Se guarda el tiempo de inicio
    minimo_manual = min_manual(numeros_total[i])    #Se ejecuta la función manual
    tiempo = time.time() - inicio                   #Se realiza el calculo para ver el tiempo transcurrido
    print(f"{10**(i+3)} {tiempo:.10f}")






