import time
import random

def generar_lista_aleatoria(cantidad):
    # Usamos números hasta 999 para ver mejor el efecto de unidades/decenas/centenas
    return [random.randint(1, 999) for _ in range(cantidad)]

def counting_sort_por_digito(arr, exp):
    n = len(arr)
    salida = [0] * n
    conteo = [0] * 10  # 10 cubetas (dígitos 0 al 9)
    
    # 1. Contar ocurrencias según el dígito (exp)
    for i in range(n):
        index = (arr[i] // exp)
        digito = index % 10
        conteo[digito] += 1
    
    # 2. Transformar conteo a posiciones reales (acumulativo)
    for i in range(1, 10):
        conteo[i] += conteo[i - 1]
    
    # 3. Construir el array de salida
    # Se recorre al revés para mantener la estabilidad (orden relativo)
    i = n - 1
    while i >= 0:
        index = (arr[i] // exp)
        digito = index % 10
        salida[conteo[digito] - 1] = arr[i]
        conteo[digito] -= 1
        i -= 1
    
    # 4. Copiar salida al array original
    for i in range(n):
        arr[i] = salida[i]

def ejecutar_radix_sort(lista):
    print(f"\n--- Inicio Radix Sort ---")
    print(f"Lista original: {lista}")
    
    inicio = time.perf_counter()
    
    # Encontrar el número máximo para saber cuántos dígitos tiene
    maximo = max(lista)
    
    # Hacemos el counting sort para cada dígito.
    # exp es 1 (unidades), 10 (decenas), 100 (centenas)...
    exp = 1
    paso = 1
    while maximo // exp > 0:
        print(f"\n> Paso {paso}: Ordenando por el dígito de las {'unidades' if exp==1 else 'decenas' if exp==10 else 'centenas' if exp==100 else 'miles'} (exp={exp})")
        
        counting_sort_por_digito(lista, exp)
        
        print(f"  Resultado parcial: {lista}")
        exp *= 10
        paso += 1
        
    fin = time.perf_counter()
    return lista, fin - inicio

if __name__ == "__main__":
    try:
        entrada = input("¿Cuántos números aleatorios para Radix Sort? ")
        cantidad = int(entrada)
        datos = generar_lista_aleatoria(cantidad)
        
        lista_ordenada, tiempo = ejecutar_radix_sort(datos)
        
        print("\n" + "="*40)
        print(f"Resultado Final: {lista_ordenada}")
        print(f"Tiempo de ejecución: {tiempo:.6f} segundos")
        print("="*40)
    except ValueError:
        print("Entrada no válida.")