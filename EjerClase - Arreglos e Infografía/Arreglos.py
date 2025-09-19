import random
import time

# 1. Crear la matriz (6 materias x 500 alumnos)
materias_alumnos = [[0 for alumno in range(500)] for materia in range(6)]

# 2. Llenar la matriz con calificaciones aleatorias
for i in range(6):  # filas → materias
    for j in range(500):  # columnas → alumnos
        materias_alumnos[i][j] = random.randint(0, 100)

# 3. Definir indices (Materia 5, Alumno 321)
materia = 4   # índice 4 = Materia 5
alumno = 320  # índice 320 = Alumno 321

# 4. Medir tiempo de acceso
inicio = time.time()
calificacion = materias_alumnos[materia][alumno]
fin = time.time()

print(f"Calificación del Alumno {alumno+1} en Materia {materia+1}: {calificacion}")
print(f"Tiempo de acceso: {fin - inicio:.10f} segundos")
