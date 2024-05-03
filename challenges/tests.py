s = 'this is a sentence'
print(s.capitalize())
print(s)

# Forma pythonic
q = 'this is a sentence'. capitalize()
print(q)

print(s.count('i'))

pre = 'unhappy'
suf = 'quickly'
print(pre.startswith('un'))
print(pre.endswith('ly'))
print(suf.endswith('ly'))

# Find
print(s.find('i'))   # Retorna la primera posición en la que se encuentra la i

print(s[s.find('i')])

# Upper (mayusculas)
print(s.upper())

# Cambiar minusculas por mayusculas y viceversa
m = 'sCreAm'
print(m.swapcase())

# Hacer mayuscula cada palabra inicial de una oración
print(s.title())

# Te dice si está en mayusucula o minuscula
print(s.isupper())
print(s.islower())

# Isalnum
a = '12expos2'
print(a.isalnum())

# isalpha
b = '1232dkd'
print(b.isalpha())

# isdecimal NO ENETIENDO
c = '[clase10 perfecta]'
print(c.isdecimal())

# is digit
d = '2029'
print(d.isdigit())

# isnumeric
e = '103293930'
print(e.isnumeric())

# istitle
print(s.istitle())

# isspace
print(s.isspace())
f = ' '
print(f.isspace())

# Is trip
g = 'mucho   espacio  q'
print(g.lstrip())

# APUNTE DE LISTAS
# Con variable
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list[0] = 'sin(x)'
print(my_list)
my_list[1] = 'cos(x)'
print(my_list)
my_list[2] = 'tan(x)'
print(my_list)

# Con iterable (tupla, lista o string)
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list[0:3] = ['sin(x)', 'cos(x)', 'tan(x)']
print(my_list)

# Iterable con el paso que se va a dar
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list[0:5:2] = ['sin(x)', 'cos(x)', 'tan(x)']
print(my_list)

# Remover elementos del slide
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
del my_list[0]
print(my_list)
del my_list[0:3]
print(my_list)

# Extender la secuencia con los contenidos del iterable
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list += ['python', 'C', 'R']
print(my_list)

# Actualiza la secuencia con el contenido repetido n veces
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_list *= 2
print(my_list)

# MÉTODOS DE LISTAS

# Append
fruits = []
print(fruits)
fruits.append('apple')
fruits.append('grape')
print(fruits)

# Clear
fruits.clear()
print(fruits)

# Copy
authors = ['Mood', 'Bowers', 'Apostol']
at_copy = authors.copy()
print(at_copy)
print(id(at_copy))
print(id(authors))

# Otra forma de hacer la copia
authors = ['Mood', 'Bowers', 'Apostol']
at_copy = authors[:]

# Extend
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
print(my_list)
my_variable = my_list.extend(['python', 'C', 'R'])
print(my_variable)

# Insert
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
my_list.insert(1, 'arctan')
print(my_list)

# Popped
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
popped = my_list.pop()
print(popped, my_list)
popped = my_list.pop(0)
print(popped, my_list)

# Remove: elimina el primer objeto x de la lista
words = ['red', 'read', 'red']
words.remove('red')
words.remove('red')
print(words)

# Reverse: cambia el orden del final al inicio
my_list = ['sin', 'cos', 'tan', 'f(x)', 'g(x)']
my_list.reverse()
print(my_list)
print(sorted(my_list))

# Sort
my_list = [45, -8, 54.14, 3.14, 0]
# my_list.sort()
print(sorted(my_list))
print(my_list)

# Count
my_list = [45, -8, 54.14, 3.14, 0, 0, 0]
print(my_list.count(0))

print('jajaja'.count('j'))

# Index: retrona en que indice está el objeto
my_list = [45, -8, 54.14, 3.14, 0, 0, 0]
print(my_list.index(0))
print('jajaja'.index('j'))
