"""
create a program that computes the average of a collection of values entered by the user.
The user will enter 0 as a sentinel value to indicate that no further values will be provided.
Your program should display an appropriate error message if the first value entered by the user is 0.
"""

print('Ingrese a continuación los valores de los que desea obtener su promedio.')
print('Para terminar, indique con un 0')

coleccion = []

while True:
    valores = float(input('Ingrese el valor: '))
    if valores == 0:
        if len(coleccion) == 0:
            print('Ha ocurrido un error, por favor ingrese al menos un valor diferente de 0')
            continue
        else:
            break
    coleccion.append(valores)

total = sum(coleccion)
mean = total / len(coleccion)
print(f'El promedio de todos los valores indicados en la coleccion es {mean}')