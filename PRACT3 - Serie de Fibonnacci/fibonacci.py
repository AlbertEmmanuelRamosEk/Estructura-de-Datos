# Serie de Fibonacci

def fibonacci(n):
    a, b = 0, 1
    for i in range(n):
        print(a, end=" ")
        a, b = b, a + b

num = int(input("¿Cuántos términos de la serie de Fibonacci deseas? "))

print("Serie de Fibonacci:")
fibonacci(num)
