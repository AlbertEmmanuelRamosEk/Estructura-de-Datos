import re

class Cola:
    def __init__(self):
        self.elementos = []

    # API "original"
    def agregar(self, elemento):
        self.elementos.append(elemento)

    def eliminar(self):
        if self.elementos:
            return self.elementos.pop(0)
        return None

    def esta_vacia(self):
        return len(self.elementos) == 0

    # Métodos con nombres que usa SistemaServicios
    def encolar(self, elemento):
        # alias a agregar
        return self.agregar(elemento)

    def desencolar(self):
        # alias a eliminar
        return self.eliminar()

    def to_list(self):
        # representación como lista (no modifica la cola)
        return list(self.elementos)

    def __repr__(self):
        return f"Cola({self.elementos})"


class SistemaServicios:
    def __init__(self):
        # diccionario: servicio_numero (int) -> Cola de tickets
        self.colas = {}
        # contador por servicio para asignar el siguiente número de ticket
        self.contadores = {}

    def _obtener_cola(self, servicio):
        if servicio not in self.colas:
            self.colas[servicio] = Cola()
            self.contadores[servicio] = 0
        return self.colas[servicio]

    def llegada(self, servicio: int):
        cola = self._obtener_cola(servicio)
        # asignar siguiente número de ticket
        self.contadores[servicio] += 1
        ticket = self.contadores[servicio]
        cola.encolar(ticket)   # ahora existe en Cola
        return ticket

    def atender(self, servicio: int):
        if servicio not in self.colas or self.colas[servicio].esta_vacia():
            return None
        return self.colas[servicio].desencolar()

    def estado(self):
        # devuelve una representación simple del estado actual
        return {s: self.colas[s].to_list() for s in sorted(self.colas)}


# Interfaz de consola simple
def interfaz_consola():
    sistema = SistemaServicios()
    print("Sistema de colas de servicios. Comandos:")
    print("  C<n>  -> llegada de cliente al servicio n (ej: C2 o C 2)")
    print("  A<n>  -> atender cliente del servicio n (ej: A2 o A 2)")
    print("  E     -> mostrar estado actual")
    print("  Q     -> salir")
    print()

    while True:
        entrada = input("Ingrese comando: ").strip().upper()
        if entrada == "":
            continue
        if entrada == "Q":
            print("Saliendo...")
            break
        if entrada == "E":
            print("Estado actual de colas:", sistema.estado())
            continue

        # aceptar formatos C2, C 2, A2, A 2
        m = re.match(r"^([CA])\s*([0-9]+)$", entrada)
        if not m:
            print("Comando no reconocido. Intente C<n> o A<n> (por ejemplo: C1, A2).")
            continue

        tipo, serv_str = m.group(1), m.group(2)
        servicio = int(serv_str)

        if tipo == "C":
            ticket = sistema.llegada(servicio)
            print(f"Cliente agregado al servicio {servicio}. Ticket: {ticket}")
        else:  # tipo == "A"
            atendido = sistema.atender(servicio)
            if atendido is None:
                print(f"No hay clientes en la cola del servicio {servicio}.")
            else:
                print(f"Atendiendo servicio {servicio}: llamando ticket {atendido}.")

# Ejecutar la interfaz
if __name__ == "__main__":
    interfaz_consola()
