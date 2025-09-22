class GestionVentas:
    """
    Clase para gestionar ventas mensuales por departamento usando un arreglo 12x3.
    Filas: 0=Enero, 1=Febrero, ..., 11=Diciembre
    Columnas: 0=Ropa, 1=Deportes, 2=Juguetería
    """

    def __init__(self):
        # Arreglo bidimensional para almacenar las ventas. Inicializa 12 filas x 3 columnas con 0.0
        # self.ventas[mes][departamento] -> monto (double/float)
        self.ventas = [[0.0 for _ in range(3)] for _ in range(12)]

        # Lista con los nombres de los meses (índices 0..11)
        self.nombres_meses = [
            "Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
            "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"
        ]

        # Lista con los nombres de los departamentos (índices 0..2)
        self.nombres_departamentos = ["Ropa", "Deportes", "Juguetería"]

    def insertar_venta(self, mes, departamento, monto):
        """
        Inserta o actualiza un elemento en el arreglo de ventas.
        :param mes: Índice del mes (0-11).
        :param departamento: Índice del departamento (0-2).
        :param monto: El monto de la venta a insertar.
        """
        # Validación de índices: mes entre 0 y 11; departamento entre 0 y 2
        if 0 <= mes < 12 and 0 <= departamento < 3:
            # Asigna el monto en la posición indicada
            self.ventas[mes][departamento] = monto
            # Mensaje de confirmación con nombres legibles
            print(f"Venta de {self.nombres_meses[mes]} en {self.nombres_departamentos[departamento]} actualizada a: {monto}")
        else:
            # Mensaje de error en caso de índices fuera de rango
            print("Error: Índices de mes o departamento fuera de rango.")

    def buscar_venta(self, mes, departamento):
        """
        Busca un elemento particular en el arreglo.
        :param mes: Índice del mes (0-11).
        :param departamento: Índice del departamento (0-2).
        :return: El monto de la venta si se encuentra, o -1.0 si los índices son inválidos.
        """
        # Validación de índices como en insertar_venta
        if 0 <= mes < 12 and 0 <= departamento < 3:
            # Recupera el monto almacenado
            monto = self.ventas[mes][departamento]
            # Muestra mensaje indicando el resultado de la búsqueda
            print(f"Venta encontrada para {self.nombres_meses[mes]} en {self.nombres_departamentos[departamento]}: {monto}")
            return monto
        else:
            # Si índices inválidos, informa y devuelve un valor centinela (-1.0)
            print("Error: Índices de mes o departamento fuera de rango. No se pudo buscar la venta.")
            return -1.0

    def eliminar_venta(self, mes, departamento):
        """
        Elimina una venta en particular de algún departamento (estableciéndola a 0.0).
        :param mes: Índice del mes (0-11).
        :param departamento: Índice del departamento (0-2).
        """
        # Validación de índices
        if 0 <= mes < 12 and 0 <= departamento < 3:
            # Guarda el valor anterior (por si se desea mostrar)
            venta_anterior = self.ventas[mes][departamento]
            # Establece la celda a 0.0 para "eliminar" la venta
            self.ventas[mes][departamento] = 0.0
            # Mensaje informando la eliminación y el valor anterior
            print(
                f"Venta de {self.nombres_meses[mes]} en {self.nombres_departamentos[departamento]} "
                f"(anteriormente: {venta_anterior}) eliminada. Ahora es: {self.ventas[mes][departamento]}"
            )
        else:
            # Mensaje de error si índices inválidos
            print("Error: Índices de mes o departamento fuera de rango. No se pudo eliminar la venta.")

    def imprimir_arreglo(self):
        """
        Imprime el contenido actual de todo el arreglo de ventas en formato tabular.
        """
        # Título del resumen
        print("\n--- Resumen de Ventas Mensuales ---")

        # Cabecera: primer campo "Mes/Depto." y luego los nombres de los departamentos
        print(f"{'Mes/Depto.':<15}", end="")
        for dept in self.nombres_departamentos:
            # Imprime cada nombre de departamento alineado a la izquierda en 15 caracteres
            print(f"{dept:<15}", end="")
        print()  # Salto de línea después de la cabecera

        # Recorre cada mes (fila)
        for i in range(12):
            # Imprime nombre del mes alineado
            print(f"{self.nombres_meses[i]:<15}", end="")
            # Imprime los montos de los 3 departamentos formateados con 2 decimales
            for j in range(3):
                print(f"{self.ventas[i][j]:<15.2f}", end="")
            print()  # Salto de línea al terminar la fila del mes

        # Línea separadora al final del resumen
        print("-----------------------------------\n")


# Ejemplo de uso:
if __name__ == "__main__":
    gv = GestionVentas()  # Crea la instancia que maneja las ventas

    # Imprimir el arreglo vacío al inicio
    gv.imprimir_arreglo()

    # 1. Insertar elementos
    print("--- Insertando Ventas ---")
    gv.insertar_venta(0, 0, 1500.50)   # Enero, Ropa
    gv.insertar_venta(0, 1, 800.25)    # Enero, Deportes
    gv.insertar_venta(0, 2, 2100.00)   # Enero, Juguetería
    gv.insertar_venta(1, 0, 1200.00)   # Febrero, Ropa
    gv.insertar_venta(11, 2, 3500.75)  # Diciembre, Juguetería (ejemplo)
    gv.insertar_venta(12, 0, 100.00)   # Intento de insertar con índice de mes fuera de rango (genera mensaje de error)

    gv.imprimir_arreglo()  # Mostrar el arreglo después de las inserciones

    # 2. Buscar un elemento
    print("--- Buscando Ventas ---")
    gv.buscar_venta(0, 0)   # Buscar Enero, Ropa
    gv.buscar_venta(1, 1)   # Buscar Febrero, Deportes (si no se insertó, será 0.0)
    gv.buscar_venta(11, 2)  # Buscar Diciembre, Juguetería
    gv.buscar_venta(5, 5)   # Intento de buscar con índice de departamento fuera de rango (error)

    # 3. Eliminar una venta
    print("--- Eliminando Ventas ---")
    gv.eliminar_venta(0, 1)  # Eliminar Enero, Deportes
    gv.eliminar_venta(1, 0)  # Eliminar Febrero, Ropa
    gv.eliminar_venta(1, 5)  # Intento de eliminar con índice de departamento fuera de rango (error)

    gv.imprimir_arreglo()  # Mostrar el arreglo después de las eliminaciones
