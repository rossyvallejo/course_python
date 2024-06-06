import math as mt
import numpy as np

# 1) Crear las funciones en python
eu = mt.exp(1)

def f(n):
    if n >= 0:
        result = n / 3
    else:
        result = -(n + 5) / 6
    return result

def g(x):
    if x < 0:
        res_2 = pow(x, 1/2)
    elif 0 <= x < 1:
        res_2 = 4 * mt.cos(2 * mt.pi * x)
    else:
        res_2 = x * mt.log((pow(eu, x) * mt.tanh(x)),2)
    return res_2

# 2)

# Parámetros
mu = 2
sigma = np.sqrt(5)
num_samples = 10000

# Generar números aleatorios de la distribución normal
random_numbers = np.random.normal(mu, sigma, num_samples)


random_numbers_list = random_numbers.tolist()
print(f' Los 10,000 valores aleatorios de la distribución normal son: {random_numbers_list}')


results_f = [f(n) for n in random_numbers_list]
results_g = [g(x) for x in random_numbers_list]

print("Resultados de f:", results_f)
print("Resultados de g:", results_g)
