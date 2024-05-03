# # Loop
# word =['a', 'b', 'c', 'd']
# for letter in word:
#     print(letter)
#
# k = 0
# while k<5:
#     print(f'The value of k is {k}')
#     k+= 1

# x = 'spam'
# while x:
#     print(x,end=' ')
#     x = x[1:]

# x = 10
# while x:
#     x-= 1
#     if x % 2 == 0:
#         continue
#     print(x)

# words = ['despair', 'phone', 'computer', 'english']
# # k = -len(words)
# # while words:
# #     print(words[k])
# #     del words[k]
# #     k += 1
# #     print(words)
#
# print(words.__getitem__(0))
# # la linea anterior es lo mismo que
# print(words[0])
#
# words = ['despair', 'phone', 'computer', 'english', 'science']
#
# for index in range(0, len(words)):
#     print(words[index])
#
# # forma pythonic de hacerlo:
# for letter in words:
#     print(letter)

# Ejercicio
"""
objective: write a program that repeatedly asks the user to enter a number. If the number is positive, ass it to a running total, 
if the number is negative, stop the loop and ptinr the final totak"""


suma = 0
while True:
    number = int(input('Ingresa un número: '))
    if number < 0:
        print(suma)
        break
    suma += number

