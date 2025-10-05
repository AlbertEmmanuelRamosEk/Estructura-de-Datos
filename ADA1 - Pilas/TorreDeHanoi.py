def Torre_Hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print("Mover disco 1 desde", origen, "hacia", destino)
        return 1
    else:
        combinaciones = 0
        combinaciones += Torre_Hanoi(n-1, origen, auxiliar, destino)
        print("Mover disco", n, "desde", origen, "hacia", destino)
        combinaciones += 1
        combinaciones += Torre_Hanoi(n-1, auxiliar, destino, origen)
        return combinaciones
    
n = int(input("Ingrese el número de discos en la torre:"))
total_combinaciones = Torre_Hanoi(n, 'A', 'B', 'C')
print(f"Total de movimientos: {total_combinaciones}")

        