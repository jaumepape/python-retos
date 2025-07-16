def fibonacci(n):
    if n <= 0:
        return []
    elif n == 1:
        return [0]
    else:
        secuencia = [0, 1]
        for _ in range(2, n):
            siguiente_numero = secuencia[-1] + secuencia[-2]
            secuencia.append(siguiente_numero)
        return secuencia
numero_de_terminos = 10
print(f"Secuencia de Fibonacci hasta el término {numero_de_terminos}: {fibonacci_hasta_10}")