import random

"""
THE LOGIC:
1. WE NEED A DICE
2. WE ROLL THAT DICE A NUMBER OF TIME AND RECORD THE FACE OF INTEREST
3. WE COMPUTE THE FREQUENCY (NUMBER OF TIMES OUR FACE OF INTEREST RESULTED/TOTAL ROLL DICE)
"""

# paradigmas

#PROCEDURAL APPROACH

# generating the faces of a die
faces = []
for f in range(1, 7):
    faces.append(f)

print(faces)

#REPEATEDLY CHOICE a face from the list until reach some n
# count the number ocurrences the face selected

n = 100
face_selected = 5
ocurrence = 0
for _ in range(n):
    random_face = random.choice(faces)
    if face_selected == random_face:
        ocurrence += 1

# print the ratio of ocurrence (frequency)
print(f'The frequency of face number {face_selected} in {n} trials is {ocurrence/n}')


#functional aproach

# otra forma de crear una lista
faces = [f for f in range(1, 7)]

# Va a retornar un elemento aleatorio de la lista faces
def roll_dice():

    return random.choice(faces)
my_random = roll_dice()
print(my_random)

# Tirar el dsdo varias veces y registrar las caras de interés

def rolling(r, face):
    time = 0
    for _ in range(r):
        if roll_dice() == face:
            time += 1
    return time

print(rolling(5, 1))

# Definir la frecuencia
def frequency(r, face):
    print(f'The frequency is: {rolling(r, face)/ r}')

n = int(input('How many trials do you want?: '))
user_face = int(input('What face?: '))

frequency(n, user_face)

