import java.util.Scanner; // Importa la clase Scanner para entrada de datos por consola

public class GestionVentas { // Definición de la clase principal

    // Arreglo bidimensional para almacenar las ventas
    // Filas: representan los meses (0=Enero, 11=Diciembre)
    // Columnas: representan los departamentos (0=Ropa, 1=Deportes, 2=Juguetería)
    private double[][] ventas;

    // Arreglo con los nombres de los meses
    private String[] nombresMeses = {"Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                                    "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"};

    // Arreglo con los nombres de los departamentos
    private String[] nombresDepartamentos = {"Ropa", "Deportes", "Juguetería"};

    // Constructor de la clase
    public GestionVentas() {
        // Inicializar el arreglo de 12 meses x 3 departamentos
        ventas = new double[12][3];

        // Inicializar todas las ventas a 0.0 (esto ya ocurre por defecto en Java,
        // pero se hace explícito aquí para mayor claridad)
        for (int i = 0; i < 12; i++) {
            for (int j = 0; j < 3; j++) {
                ventas[i][j] = 0.0;
            }
        }
    }

    /**
     * Inserta o actualiza un elemento en el arreglo de ventas.
     * @param mes Índice del mes (0-11).
     * @param departamento Índice del departamento (0-2).
     * @param monto El monto de la venta a insertar.
     */
    public void insertarVenta(int mes, int departamento, double monto) {
        // Validar índices dentro de rango
        if (mes >= 0 && mes < 12 && departamento >= 0 && departamento < 3) {
            // Insertar/actualizar el monto en la celda correspondiente
            ventas[mes][departamento] = monto;
            // Mensaje de confirmación
            System.out.println("Venta de " + nombresMeses[mes] + " en " 
                               + nombresDepartamentos[departamento] 
                               + " actualizada a: " + monto);
        } else {
            // Mensaje de error si los índices son inválidos
            System.out.println("Error: Indices de mes o departamento fuera de rango.");
        }
    }

    /**
     * Busca un elemento particular en el arreglo.
     * @param mes Índice del mes (0-11).
     * @param departamento Índice del departamento (0-2).
     * @return El monto de la venta si se encuentra, o -1.0 si los índices son inválidos.
     */
    public double buscarVenta(int mes, int departamento) {
        if (mes >= 0 && mes < 12 && departamento >= 0 && departamento < 3) {
            // Recupera el monto en la celda indicada
            double monto = ventas[mes][departamento];
            System.out.println("Venta encontrada para " + nombresMeses[mes] 
                               + " en " + nombresDepartamentos[departamento] 
                               + ": " + monto);
            return monto;
        } else {
            // Retorna -1.0 como indicador de error si los índices son inválidos
            System.out.println("Error: Indices de mes o departamento fuera de rango. No se pudo buscar la venta.");
            return -1.0;
        }
    }

    /**
     * Elimina una venta en particular de algún departamento (estableciéndola a 0.0).
     * @param mes Índice del mes (0-11).
     * @param departamento Índice del departamento (0-2).
     */
    public void eliminarVenta(int mes, int departamento) {
        if (mes >= 0 && mes < 12 && departamento >= 0 && departamento < 3) {
            // Guarda la venta anterior antes de eliminar
            double ventaAnterior = ventas[mes][departamento];
            // Establece el valor en 0.0 (considerado como eliminado)
            ventas[mes][departamento] = 0.0;
            // Mensaje informando el cambio
            System.out.println("Venta de " + nombresMeses[mes] + " en " 
                               + nombresDepartamentos[departamento] 
                               + " (anteriormente: " + ventaAnterior 
                               + ") eliminada. Ahora es: " + ventas[mes][departamento]);
        } else {
            System.out.println("Error: Indices de mes o departamento fuera de rango. No se pudo eliminar la venta.");
        }
    }

    /**
     * Imprime el contenido actual de todo el arreglo de ventas en formato tabular.
     */
    public void imprimirArreglo() {
        System.out.println("\n--- Resumen de Ventas Mensuales ---");

        // Imprimir encabezado de la tabla
        System.out.printf("%-15s", "Mes/Depto.");
        for (String dept : nombresDepartamentos) {
            System.out.printf("%-15s", dept);
        }
        System.out.println();

        // Imprimir cada fila (mes) con sus ventas
        for (int i = 0; i < 12; i++) {
            System.out.printf("%-15s", nombresMeses[i]);
            for (int j = 0; j < 3; j++) {
                System.out.printf("%-15.2f", ventas[i][j]); // Formato con 2 decimales
            }
            System.out.println();
        }
        System.out.println("-----------------------------------\n");
    }

    // Método principal para ejecutar el programa
    public static void main(String[] args) {
        GestionVentas gv = new GestionVentas(); // Crear objeto de gestión de ventas
        Scanner scanner = new Scanner(System.in); // Crear scanner (aunque no se usa en este ejemplo)

        // Mostrar el arreglo vacío al inicio
        gv.imprimirArreglo();

        // 1. Insertar elementos de prueba
        System.out.println("--- Insertando Ventas ---");
        gv.insertarVenta(0, 0, 1500.50); // Enero, Ropa
        gv.insertarVenta(0, 1, 800.25);  // Enero, Deportes
        gv.insertarVenta(0, 2, 2100.00); // Enero, Juguetería
        gv.insertarVenta(1, 0, 1200.00); // Febrero, Ropa
        gv.insertarVenta(11, 2, 3500.75); // Diciembre, Juguetería
        gv.insertarVenta(12, 0, 100.00); // Error: mes fuera de rango

        // Imprimir arreglo tras inserciones
        gv.imprimirArreglo();

        // 2. Buscar ventas
        System.out.println("--- Buscando Ventas ---");
        gv.buscarVenta(0, 0);  // Enero, Ropa
        gv.buscarVenta(1, 1);  // Febrero, Deportes (si no se insertó, será 0.0)
        gv.buscarVenta(11, 2); // Diciembre, Juguetería
        gv.buscarVenta(5, 5);  // Error: departamento fuera de rango

        // 3. Eliminar ventas
        System.out.println("--- Eliminando Ventas ---");
        gv.eliminarVenta(0, 1); // Eliminar Enero, Deportes
        gv.eliminarVenta(1, 0); // Eliminar Febrero, Ropa
        gv.eliminarVenta(1, 5); // Error: departamento fuera de rango

        // Imprimir arreglo tras eliminaciones
        gv.imprimirArreglo();

        // Cerrar el scanner (buena práctica, aunque aquí no se usa)
        scanner.close();
    }
}
