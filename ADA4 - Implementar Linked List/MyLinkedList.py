class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class MyLinkedList:
    def __init__(self):
        self.head = None

    def estaVacia(self):
        return self.head == None

    def agregar(self, data):
        temp = Node(data)
        temp.next = self.head  
        self.head = temp

    def cantidad(self):
        actual = self.head
        contador = 0
        while actual != None:
            contador += 1
            actual = actual.next
        return contador

    def verLista(self):
        actual = self.head
        cadena = ""
        while actual != None:
            cadena += "->" + "["+ str(actual.data) +"]" 
            actual = actual.next
        return cadena 
    
    def buscar(self, data):
        actual = self.head
        while actual != None:
            if actual.data == data:
                return True
            else:
                actual = actual.next
        return False
    
    def eliminar(self, data):
        actual = self.head
        previo = None
        encontrado = False
        while actual != None and not encontrado:
            if actual.data == data:
                encontrado = True
            else:
                previo = actual
                actual = actual.next
        if actual != None:
            if previo == None:
                self.head = actual.next
            else:
                previo.next = actual.next

lista = MyLinkedList()

lista.agregar(1)
lista.agregar(2)
lista.agregar(3)
lista.agregar("Hola")
lista.agregar(4)
lista.agregar(5)

print(lista.cantidad())
print(lista.verLista())

print(lista.buscar(3))
print(lista.buscar(10))
print(lista.buscar("Hola"))

lista.eliminar(3)
print(lista.verLista()) 