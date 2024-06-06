names = ['jake', 'esteban', 'fred', 'Tim']  # lista
corrected_names = map(lambda name: name.title(), names)  # iterator

print(list(corrected_names))

for item in corrected_names:
    print(item)

for item in map(
    lambda x, y: 2*x**y,
    [1, 2, 3],
    [0.1, 0.2, 0.3]):
    print(item)


def my_func(*numbers):
    return numbers

a = my_func(5,7,9,20,54)
print(a)


def my_func(*numbers, **letters):
    return numbers, letters

a = my_func(5,7,9,20,54, a=1, b=5)
print(a)

# los valores de ""letters se guardan en un diccionario
