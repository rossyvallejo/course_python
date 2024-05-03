"""
Implement the Collatz Conjecture: Start with a number n, and repeatedly apply the rule n → n/2 if n is even
or n → 3n + 1 if n is odd. Print the sequence until n becomes 1.
"""
num = int(input('Introduce un número '))
while True: # Se usa while pq no sabemos cuatas operaciones vamos a hacer hasta llegar al 1
    # if number 1
    if num == 1:
        break

    # if number 2
    if num % 2 == 0:
        num = num/2
        print(num)
    else:
        num = 3*num + 1
        print(num)

