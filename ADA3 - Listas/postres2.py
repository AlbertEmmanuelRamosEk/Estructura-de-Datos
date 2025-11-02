class NodoIngrediente:
    def __init__(self, nombre):
        self.nombre = nombre
        self.siguiente = None


class NodoPostre:
    def __init__(self, nombre):
        self.nombre = nombre
        self.ingredientes = None  # Apunta a la lista enlazada de ingredientes
        self.siguiente = None     # Apunta al siguiente postre


class ListaPostres:
    def __init__(self):
        self.cabeza = None

    # -------------------------------
    # ALTA DE POSTRE
    # -------------------------------
    def alta_postre(self, nombre, ingredientes):
        # Evitar agregar duplicados desde el inicio
        if self.existe_postre(nombre):
            print(f"⚠️ El postre '{nombre}' ya existe. No se agregó.")
            return
        nuevo_postre = NodoPostre(nombre.title())
        for ing in ingredientes:
            self.insertar_ingrediente(nuevo_postre, ing)
        nuevo_postre.siguiente = self.cabeza
        self.cabeza = nuevo_postre
        print(f"✅ Postre '{nombre}' agregado correctamente.")

    # -------------------------------
    # VERIFICAR SI POSTRE YA EXISTE
    # -------------------------------
    def existe_postre(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre.lower():
                return True
            actual = actual.siguiente
        return False

    # -------------------------------
    # MOSTRAR INGREDIENTES DE UN POSTRE
    # -------------------------------
    def mostrar_ingredientes(self, nombre):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre.lower():
                print(f"Ingredientes de {actual.nombre}:")
                ing = actual.ingredientes
                if not ing:
                    print("   (sin ingredientes)")
                while ing:
                    print("  -", ing.nombre)
                    ing = ing.siguiente
                return
            actual = actual.siguiente
        print("❌ Postre no encontrado.")

    # -------------------------------
    # INSERTAR INGREDIENTE EN UN POSTRE (INTERNA)
    # -------------------------------
    def insertar_ingrediente(self, postre, nombre_ingrediente):
        nuevo_ing = NodoIngrediente(nombre_ingrediente.lower())
        nuevo_ing.siguiente = postre.ingredientes
        postre.ingredientes = nuevo_ing

    # -------------------------------
    # AGREGAR INGREDIENTE A UN POSTRE EXISTENTE
    # -------------------------------
    def agregar_ingrediente_a_postre(self, nombre_postre, nombre_ing):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre_postre.lower():
                self.insertar_ingrediente(actual, nombre_ing)
                print("✅ Ingrediente agregado correctamente.")
                return
            actual = actual.siguiente
        print("❌ Postre no encontrado.")

    # -------------------------------
    # ELIMINAR INGREDIENTE
    # -------------------------------
    def eliminar_ingrediente(self, nombre_postre, nombre_ing):
        actual = self.cabeza
        while actual:
            if actual.nombre.lower() == nombre_postre.lower():
                prev = None
                ing = actual.ingredientes
                while ing:
                    if ing.nombre == nombre_ing.lower():
                        if prev:
                            prev.siguiente = ing.siguiente
                        else:
                            actual.ingredientes = ing.siguiente
                        print("✅ Ingrediente eliminado.")
                        return
                    prev = ing
                    ing = ing.siguiente
                print("❌ Ingrediente no encontrado.")
                return
            actual = actual.siguiente
        print("❌ Postre no encontrado.")

    # -------------------------------
    # BAJA DE POSTRE
    # -------------------------------
    def baja_postre(self, nombre):
        actual = self.cabeza
        anterior = None
        while actual:
            if actual.nombre.lower() == nombre.lower():
                if anterior:
                    anterior.siguiente = actual.siguiente
                else:
                    self.cabeza = actual.siguiente
                print(f"✅ Postre '{nombre}' eliminado.")
                return
            anterior = actual
            actual = actual.siguiente
        print("❌ Postre no encontrado.")

    # -------------------------------
    # ELIMINAR DUPLICADOS DE POSTRES
    # -------------------------------
    def eliminar_postres_duplicados(self):
        actual = self.cabeza
        vistos = set()
        anterior = None
        while actual:
            nombre = actual.nombre.lower()
            if nombre in vistos:
                # Eliminar postre duplicado
                anterior.siguiente = actual.siguiente
            else:
                vistos.add(nombre)
                anterior = actual
            actual = actual.siguiente
        print("✅ Postres duplicados eliminados correctamente.")

    # -------------------------------
    # ELIMINAR DUPLICADOS DE INGREDIENTES (OPCIONAL)
    # -------------------------------
    def eliminar_ingredientes_duplicados(self):
        actual_postre = self.cabeza
        while actual_postre:
            vistos = set()
            previo_ing = None
            actual_ing = actual_postre.ingredientes
            while actual_ing:
                if actual_ing.nombre in vistos:
                    # Eliminar el nodo duplicado
                    previo_ing.siguiente = actual_ing.siguiente
                else:
                    vistos.add(actual_ing.nombre)
                    previo_ing = actual_ing
                actual_ing = actual_ing.siguiente
            actual_postre = actual_postre.siguiente
        print("✅ Ingredientes duplicados eliminados correctamente en todos los postres.")

    # -------------------------------
    # MOSTRAR TODOS LOS POSTRES E INGREDIENTES
    # -------------------------------
    def mostrar_todo(self):
        actual = self.cabeza
        if not actual:
            print("(No hay postres en la lista)")
        while actual:
            print(f"\n🍰 {actual.nombre}:")
            ing = actual.ingredientes
            if not ing:
                print("   (sin ingredientes)")
            while ing:
                print("   -", ing.nombre)
                ing = ing.siguiente
            actual = actual.siguiente


# -------------------------------
# MENÚ PRINCIPAL
# -------------------------------
def menu():
    lista = ListaPostres()
    while True:
        print("\n--- MENÚ ---")
        print("1. Alta postre")
        print("2. Mostrar ingredientes de un postre")
        print("3. Agregar ingrediente")
        print("4. Eliminar ingrediente")
        print("5. Baja postre")
        print("6. Mostrar todo")
        print("7. Eliminar duplicados de postres")
        print("8. Eliminar duplicados de ingredientes")
        print("0. Salir")

        op = input("Opción: ")
        if op == "1":
            nombre = input("Nombre del postre: ")
            ing = input("Ingredientes (separados por coma): ").split(",")
            lista.alta_postre(nombre, [i.strip() for i in ing])
        elif op == "2":
            nombre = input("Nombre del postre: ")
            lista.mostrar_ingredientes(nombre)
        elif op == "3":
            nombre = input("Nombre del postre: ")
            ing = input("Ingrediente a agregar: ")
            lista.agregar_ingrediente_a_postre(nombre, ing)
        elif op == "4":
            nombre = input("Nombre del postre: ")
            ing = input("Ingrediente a eliminar: ")
            lista.eliminar_ingrediente(nombre, ing)
        elif op == "5":
            nombre = input("Nombre del postre: ")
            lista.baja_postre(nombre)
        elif op == "6":
            lista.mostrar_todo()
        elif op == "7":
            lista.eliminar_postres_duplicados()
        elif op == "8":
            lista.eliminar_ingredientes_duplicados()
        elif op == "0":
            print("👋 Saliendo del programa...")
            break
        else:
            print("❌ Opción inválida.")


# -------------------------------
# EJECUCIÓN DEL PROGRAMA
# -------------------------------
if __name__ == "__main__":
    menu()
