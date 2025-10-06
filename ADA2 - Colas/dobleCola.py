from collections import deque
class Cola:
    def __init__(self):
        self.elementos = deque()
        
    def agregar(self, elemento):
        self.elementos.append(elemento)
        
    def eliminar(self):
        if not self.esta_vacia():
            return self.elementos.popleft()
        else:
            return None
        
    def esta_vacia(self):
        return len(self.elementos) == 0
    
    def __str__(self):
        return "Cola([" + ", ".join(map(str, self.elementos)) + "])"
    
def sumar_colas(cola1: Cola, cola2: Cola) -> Cola:
    resultado = Cola()
    while not cola1.esta_vacia() or not cola2.esta_vacia():
        elemento1 = cola1.eliminar() if not cola1.esta_vacia() else 0
        elemento2 = cola2.eliminar() if not cola2.esta_vacia() else 0
        
        suma = elemento1 + elemento2
        resultado.agregar(suma)
    return resultado
    

# Ejemplo de uso
cola1 = Cola()
cola1.agregar(3)
cola1.agregar(4)
cola1.agregar(2)
cola1.agregar(8)
cola1.agregar(12)

cola2 = Cola()
cola2.agregar(6)
cola2.agregar(2)
cola2.agregar(9)
cola2.agregar(11)
cola2.agregar(3)

resultado = sumar_colas(cola1, cola2)
print(f"la cola3 es: {resultado}")



    
    