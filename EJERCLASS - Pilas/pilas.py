lista = []

#push
lista.append("A")
lista.append("B")
lista.append("C")       
print("lista:", lista)

#peek
tope = lista[-1]
print("tope:", tope)

#pop
poppedElement = lista.pop()
print("pop:", poppedElement)

#lista despues del pop
print("lista despues del pop:", lista)

#si esta vacia
if len(lista) == 0:
    print("La lista esta vacia")
    
#tamaño
print("tamaño:", len(lista))



