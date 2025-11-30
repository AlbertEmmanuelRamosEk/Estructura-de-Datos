#Ordena la lista [64, 25, 12, 22, 11] mediante el método de Selección.

def seleccion(lista):
    n = len(lista)
    for i in range(n):
        min_idx = i  # Suponemos que este es el menor

        for j in range(i + 1, n):
            if lista[j] < lista[min_idx]:
                min_idx = j

        lista[i], lista[min_idx] = lista[min_idx], lista[i]  # Intercambio

    return lista

datos = [64, 25, 12, 22, 11]
print("Original:", datos)
print("Ordenado:", seleccion(datos))
