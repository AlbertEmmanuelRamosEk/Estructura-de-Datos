#Algoritmo de Kruskal para encontrar el árbol de expansión mínima en un grafo ponderado
'''
class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.rango[ra] < self.rango[rb]:
                self.padre[ra] = rb
            elif self.rango[rb] < self.rango[ra]:
                self.padre[rb] = ra
            else:
                self.padre[rb] = ra
                self.rango[ra] += 1
            return True
        return False


def kruskal(vertices, aristas):
    # aristas = [(peso, u, v)]
    aristas.sort()
    uf = UnionFind(vertices)
    mst = []

    for peso, u, v in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))

    return mst
'''
#Ejemplo de uso

class UnionFind:
    def __init__(self, n):
        self.padre = list(range(n))
        self.rango = [0] * n

    def find(self, x):
        if self.padre[x] != x:
            self.padre[x] = self.find(self.padre[x])
        return self.padre[x]

    def union(self, a, b):
        ra, rb = self.find(a), self.find(b)
        if ra != rb:
            if self.rango[ra] < self.rango[rb]:
                self.padre[ra] = rb
            elif self.rango[rb] < self.rango[ra]:
                self.padre[rb] = ra
            else:
                self.padre[rb] = ra
                self.rango[ra] += 1
            return True
        return False

def kruskal(vertices, aristas):
    aristas.sort()  # Ordenar por peso
    uf = UnionFind(vertices)
    mst = []

    for peso, u, v in aristas:
        if uf.union(u, v):
            mst.append((u, v, peso))

    return mst

aristas = [
    (1, 0, 1),
    (4, 0, 2),
    (2, 1, 3),
    (3, 2, 3)
]
mst = kruskal(4, aristas)

print("Árbol de expansión mínima (Kruskal):")
for u, v, peso in mst:
    print(f"{u} -- {peso} -- {v}")
