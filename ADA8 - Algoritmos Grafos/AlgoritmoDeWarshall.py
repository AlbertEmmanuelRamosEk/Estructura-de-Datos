#Algoritmo de Warshall para encontrar el alcance de los nodos en un grafo dirigido
'''
def warshall(matriz):
    n = len(matriz)

    alcance = [fila[:] for fila in matriz]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcance[i][j] = alcance[i][j] or (alcance[i][k] and alcance[k][j])

    return alcance
'''
#Ejemplo de uso
def warshall(matriz):
    n = len(matriz)
    alcance = [fila[:] for fila in matriz]

    for k in range(n):
        for i in range(n):
            for j in range(n):
                alcance[i][j] = alcance[i][j] or (alcance[i][k] and alcance[k][j])

    return alcance

matriz = [
    [0, 1, 0],  # A
    [0, 0, 1],  # B
    [0, 0, 0]   # C
]

resultado = warshall(matriz)

print("Matriz de alcanzabilidad:")
for fila in resultado:
    print(fila)
