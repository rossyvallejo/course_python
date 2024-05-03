name = input('Escribe tu nombre: ')
print('Tu nombre es:', name)
print(type(name))

# Realizando type casting
my_num = input('Escribe un número: ')
my_num2 = input('Escribe otro numero: ')
my_num = int(my_num)
my_num2 = int(my_num2)
print(my_num + my_num2)

# Otra forma de hacerlo (es más eficiente)
my_num = int(input('Escribe un número: '))
my_num2 = int(input('Escribe otro numero: '))
print(my_num + my_num2)

# Tercera forma
my_num = input('Escribe un número: ')
my_num2 = input('Escribe otro numero: ')
print(my_num + my_num2)  # concatenation
print(int(my_num) + int(my_num2))  # suma
