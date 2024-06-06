# print(*[1,2,3])
# print([1,2,3])

days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday']  # Packing

# rest, school, free = days  # error
rest, *school, free = days
print(rest)
print(school)
print(free)


