'''Dado un arreglo de números [5, 2, 9, 1, 5, 6], ordénalo
de menor a mayor utilizando el método Burbuja.'''

def burbuja(lista):
    n = len(lista)
    for i in range(n):
        for j in range(0, n - i - 1):
            if lista[j] > lista[j + 1]:
                lista[j], lista[j + 1] = lista[j + 1], lista[j]  # Intercambio
    return lista

datos = [5, 2, 9, 1, 5, 6]
print("Original:", datos)
print("Ordenado:", burbuja(datos))
