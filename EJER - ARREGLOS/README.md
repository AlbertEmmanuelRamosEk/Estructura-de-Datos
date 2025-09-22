Explicación del Programa:

Este programa en Java gestiona las ventas mensuales de tres departamentos ("Ropa", "Deportes", "Juguetería") a lo largo de 12 meses (Enero a Diciembre). Utiliza un arreglo bidimensional (ventas) para almacenar estos datos. Además, implementa métodos para insertar, buscar y eliminar ventas, siguiendo las especificaciones del ejercicio.

Cómo funciona cada uno de los métodos:
1. insertarVenta(int mes, int departamento, double monto):

- Propósito: Este método permite añadir o actualizar el monto de una venta específica en el arreglo.

- Funcionamiento: Recibe como parámetros el mes (0 para Enero, 11 para Diciembre), el departamento (0 para Ropa, 1 para Deportes, 2 para Juguetería) y el monto de la venta.

- Realiza una validación para asegurar que los índices de mes y departamento estén dentro de los límites válidos del arreglo.

- Si los índices son válidos, asigna el monto al elemento correspondiente en el arreglo ventas[mes][departamento].

- Imprime un mensaje de confirmación o de error si los índices son inválidos.

2. buscarVenta(int mes, int departamento):

- Propósito: Permite encontrar y mostrar el monto de una venta específica.

- Funcionamiento: Toma como parámetros el mes y el departamento.

- Al igual que insertarVenta, valida los índices para evitar errores ArrayIndexOutOfBoundsException.

- Si los índices son válidos, accede al valor en ventas[mes][departamento] y lo imprime en la consola.

- En caso de índices inválidos, muestra un mensaje de error.

Nota: Este método devuelve el valor de la venta encontrada (o -1.0 si es inválido) para una posible utilización en otras partes del programa, además de imprimirlo.

3. eliminarVenta(int mes, int departamento):

- Propósito: Permite "eliminar" una venta específica, estableciendo su valor a 0.0.

- Funcionamiento: Recibe el mes y el departamento de la venta que se desea eliminar.

- Valida los índices.

- Si los índices son válidos, establece el valor de ventas[mes][departamento] a 0.0. En el contexto de un sistema de ventas, "eliminar" suele significar anular la venta o establecerla en cero, ya que eliminar físicamente el espacio de la matriz sería más complejo y no es usual para este tipo de estructuras.

- Informa al usuario si la eliminación fue exitosa o si los índices fueron inválidos.

4. imprimirArreglo():

- Propósito: Muestra el contenido actual de todo el arreglo bidimensional en un formato legible, similar a la tabla del ejercicio.

- Funcionamiento: Itera a través de las filas (meses) y columnas (departamentos) del arreglo ventas.

- Para cada celda, imprime el valor de la venta.

- Incluye encabezados para los meses y los departamentos para una mejor comprensión.
