# Generate and print the first 10 numbers in the Fibonacci sequence
secuencia = [0, 1]
for num in range(2, 10):
    fibonacci = secuencia[num - 1] + secuencia[num - 2]
    secuencia.append(fibonacci)

print("Los primeros 10 números de la secuencia de Fobonacci son: ")
for n in secuencia:
    print(n)