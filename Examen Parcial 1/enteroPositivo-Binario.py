def decimal_a_binario_recursivo(n):
    if n == 0:
        return "0"
    elif n == 1:
        return "1"
    else:
        return decimal_a_binario_recursivo(n // 2) + str(n % 2)

try:
    numero = int(input("Por favor, introduce un número entero positivo: "))
    if numero < 0:
        print("El número debe ser positivo. Por favor, inténtalo de nuevo.")
    else:
        resultado = decimal_a_binario_recursivo(numero)
        print(f"El equivalente binario de {numero} es: {resultado}")
except ValueError:
    print("Entrada no válida. Por favor, introduce un número entero.")
    
    