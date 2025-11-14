#Algoritmo de Floyd-Warshall para encontrar las rutas más cortas entre todos los pares de nodos en un grafo ponderado
'''
def floyd_warshall(grafo):
    nodos = list(grafo.keys())
    dist = {i: {j: grafo[i].get(j, float('inf')) for j in nodos} for i in nodos}

    for v in nodos:
        dist[v][v] = 0

    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist
'''
#Ejemplo de uso

grafo = {
    'A': {'A': 0, 'B': 5, 'C': 2, 'D': float('inf')},
    'B': {'A': 5, 'B': 0, 'C': float('inf'), 'D': 1},
    'C': {'A': 2, 'B': float('inf'), 'C': 0, 'D': 4},
    'D': {'A': float('inf'), 'B': 1, 'C': 4, 'D': 0}
}

def floyd_warshall(grafo):
    nodos = list(grafo.keys())
    dist = {i: {j: grafo[i][j] for j in nodos} for i in nodos}

    for k in nodos:
        for i in nodos:
            for j in nodos:
                if dist[i][j] > dist[i][k] + dist[k][j]:
                    dist[i][j] = dist[i][k] + dist[k][j]

    return dist

print("Tabla de distancias mínimas entre todos los nodos:")
distancias = floyd_warshall(grafo)

for i in distancias:
    print(i, distancias[i])
