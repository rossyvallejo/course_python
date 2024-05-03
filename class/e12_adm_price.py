"""
A particular zoo determines the price of admission based on the age of the guest.
Guests 2 years of age and less are admitted without charge.
Children between 3 and 12 years of age cost $14.00.
Seniors aged 65 years and over cost $18.00.
Admission for all other guests is $23.00. Create a program that begins by reading the ages of all the guests in a
group from the user,with one age entered on each line.
The user will enter a blank line to indicate that there are no more guests in the group.
Then your program should display the admission cost for the group with an appropriate message.
"""

print("Buen día. A continuación, ingrese las edades de los huéspedes una por línea. "
      "Presione Enter para terminar.")

edades = []
while True:
    entrada = input("Edad del huésped: ")
    if entrada == "":
        break
    edad = int(entrada)
    edades.append(edad)

def calcular_precio(edades):
    precio_total = 0
    for edad in edades:
        if edad <= 2:
            precio_total += 0
        elif 3 <= edad <= 12:
            precio_total += 14
        elif edad >= 65:
            precio_total += 18
        else:
            precio_total += 23
    return precio_total


precio_total = calcular_precio(edades)
print(f"El costo total de admisión para el grupo es: ${precio_total}")




