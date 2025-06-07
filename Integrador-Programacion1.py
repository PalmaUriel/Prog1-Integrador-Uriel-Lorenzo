import time
import random

numeros_0 = [random.randint(1, 1000000) for i in range(1000)]
numeros_1 = [random.randint(1, 1000000) for i in range(10000)]
numeros_2 = [random.randint(1, 1000000) for i in range(100000)]
numeros_3 = [random.randint(1, 1000000) for i in range(1000000)]
numeros_4 = [random.randint(1, 1000000) for i in range(10000000)]
numeros_total = [numeros_0, numeros_1, numeros_2, numeros_3, numeros_4]

def min_manual(lista):
    if not lista:                           ### 1
        return None                         
    minimo = lista[0]                       ### 1  
    for numero in lista:                    ### 2n     T(n) = 1 + 1 + 2n + 1 = 2n + 3 == O(n)
        if numero < minimo:                 ### 1
            minimo = numero                 ### 1
    return minimo                           ### 1

def min_auto(lista):
    if not lista:                           ### 1
        return None                         ### 1       T(n) = 1 + 1 + n = n + 2 == O(n)
    return min(lista)                       ### n

print("Resultados de la búsqueda del minimo automático")

for i in range(5):
    inicio = time.time()
    minimo_auto = min_auto(numeros_total[i])
    tiempo = time.time() - inicio
    print(f"{10**(i+3)} {tiempo:.10f}")

print("Resultados de la búsqueda del minimo manual")

for i in range(5):
    inicio = time.time()
    minimo_manual = min_manual(numeros_total[i])
    tiempo = time.time() - inicio
    print(f"{10**(i+3)} {tiempo:.10f}")






