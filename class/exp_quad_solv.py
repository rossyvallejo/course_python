"""
Write a lambda function that calculates the roots of a quadratic equation ax^2+bx+c=0.
Assume that the discriminant is always non-negative.
"""

def lambda_func(a, b, c):
    x1 = (-b + pow((pow(b,2)-4*a*c),1/2))/ (2*a)
    x2 = (-b - pow((pow(b,2)-4*a*c),1/2))/ (2*a)
    print(f'Las raíces de las ecuación cuadrática son: raíz 1= {x1} y raiz 2= {x2}')

lambda_func(2, 2, 0)

# Otra forma de hacerlo
quad = lambda a, b, c: ((-b + pow((pow(b,2)-4*a*c),1/2))/ (2*a), (-b - pow((pow(b,2)-4*a*c),1/2))/ (2*a))
print(quad(2, 2, 0))