#Ordena la lista [12, 11, 13, 5, 6] usando el método de Inserción.

def insercion(lista):
    for i in range(1, len(lista)):
        clave = lista[i]
        j = i - 1

        while j >= 0 and clave < lista[j]:
            lista[j + 1] = lista[j]
            j -= 1

        lista[j + 1] = clave

    return lista

datos = [12, 11, 13, 5, 6]
print("Original:", datos)
print("Ordenado:", insercion(datos))
