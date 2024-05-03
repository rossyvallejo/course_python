# Import the math module (as you want)
from math import factorial, exp, prod, sumprod

# Make the Poisson distribution. The user must enter the parameters. Then print out the result
lam = int(input('Introduce el valor de lambda: '))
k = int(input('Introduce el valor de k: '))
poisson = (pow (lam, k) * pow(exp(1), -lam)) / factorial(k)
print(f'El valor de la distribución poisson con los parámetros dados es: {poisson}')


# Make an iterable with some numbers to calculate the product of all those numbers
x = [1, 5, 6, 12, 3]
product = prod(x, start=1)
print(product)

# From two iterables, calculate the sum of the product of values
p = [2, 5, 7, 8, 9]
q = [1, 4, 5, 2, 14]

result = sumprod(p, q)
print(result)

# Calculate the GCD of two numbers that user gives



# Make the binomial distribution. The user must enter the values: n, x, p. Then print out the result



# The user enter a float number, and then the ceiling of that number must appear in the screen, as
# "the ceiling of x is y "


# Choose two functions from the math documentation to make exercises like the previous