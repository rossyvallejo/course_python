from random import gauss
my_numbers = []
for num in range(10):
    my_numbers.append(gauss())

print(my_numbers)

# ---------------------------------------------------------------------------------------------------------------------
my_numbers = [gauss() for num in range(10)]
print(my_numbers)

# ---------------------------------------------------------------------------------------------------------------------
print([gauss() for num in range(10)])