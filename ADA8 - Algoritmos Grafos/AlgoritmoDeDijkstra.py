#Algoritmo de Dijkstra para encontrar la ruta más corta en un grafo ponderado
'''
import heapq

def dijkstra(grafo, origen):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0
    pq = [(0, origen)]

    while pq:
        distancia_actual, nodo = heapq.heappop(pq)

        if distancia_actual > dist[nodo]:
            continue

        for vecino, peso in grafo[nodo].items():
            nueva_dist = distancia_actual + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(pq, (nueva_dist, vecino))

    return dist
'''
#Ejemplo de uso
'''
A --5-- B
|       |
2       1
|       |
C --4-- D
'''

import heapq
grafo = {
    'A': {'B': 5, 'C': 2},
    'B': {'A': 5, 'D': 1},
    'C': {'A': 2, 'D': 4},
    'D': {'B': 1, 'C': 4}
}

def dijkstra(grafo, origen):
    dist = {nodo: float('inf') for nodo in grafo}
    dist[origen] = 0
    pq = [(0, origen)]

    while pq:
        distancia_actual, nodo = heapq.heappop(pq)

        for vecino, peso in grafo[nodo].items():
            nueva_dist = distancia_actual + peso
            if nueva_dist < dist[vecino]:
                dist[vecino] = nueva_dist
                heapq.heappush(pq, (nueva_dist, vecino))

    return dist

print("Distancias mínimas desde A:")
print(dijkstra(grafo, 'A'))

