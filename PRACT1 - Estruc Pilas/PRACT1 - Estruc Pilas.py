class Pila:
    def __init__(self, capacidad):
        self.capacidad = capacidad
        self.elementos = []
        
    def insertar(self, elemento):
        if len(self.elementos) < self.capacidad:
            self.elementos.append(elemento)
            print(f"El elemento {elemento} ha sido agregado a la pila: {self.elementos}")
        else:
            print("La pila está excediendo su capacidad máxima (overflow).")
            
    def eliminar(self, LS):
        if len(self.elementos) > 0:
            eliminados = self.elementos.pop()
            print(f"Eliminando {eliminados} de la pila: {self.elementos}")
        else:
            print("La pila está vacía (underflow).")
            
pila = Pila(8)
pila.insertar('X')
pila.insertar('Y')       
pila.eliminar('Z')
pila.eliminar('T')   
pila.eliminar('U')
pila.insertar('V')
pila.insertar('W')
pila.eliminar('P')
pila.insertar('R')  

print(f"Pilas que quedaron: {pila.elementos}")
print(f"El tamaño de la pila es: {len(pila.elementos)}")