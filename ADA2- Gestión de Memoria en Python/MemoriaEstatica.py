calificaciones = [0] * 5  # Lista para almacenar las calificaciones de 5 estudiantes    
for i in range(5):
    calificaciones[i] = int(input(f"Ingrese la calificación del estudiante {i + 1}: "))
    
print(f"Las calificaciones ingresadas son: {calificaciones}")
