"""
Write a program that displays a temperature conversion table for degrees Celsius and degrees Fahrenheit.
The table should include rows for all temperatures between 0 and 100 degrees Celsius that are multiples of 10 degrees Celsius.
Include appropriate headings on your columns.
The formula for converting between degrees Celsius and degrees Fahrenheit can be found on the Internet.
"""

"""
Escriba un programa que muestre una tabla de conversión de temperatura para grados Celsius y grados Fahrenheit.
La tabla debe incluir filas para todas las temperaturas entre 0 y 100 grados Celsius que sean múltiplos de 10 grados Celsius.
Incluya títulos apropiados en sus columnas.
La fórmula para convertir entre grados Celsius y grados Fahrenheit se puede encontrar en Internet.
"""

print("Tabla de conversión de temperatura para °C y °F:")
print("Celsius   Fahrenheit")
print("---------------------")
for celsius in range(0, 101, 10):
    fahrenheit = (celsius * 9/5) + 32
    print(f"{celsius:^7}  {fahrenheit:^10.1f}")
