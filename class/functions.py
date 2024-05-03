def printing_star():

    print('*****************')
    print('*               *')
    print('*****************')


print(printing_star())
print(printing_star())



def printing_star(n):
    for _ in range(n):
        print('*****************')
        print('*               *')
        print('*****************')

printing_star(2)


def f(x):
    return x*x
print(f(2))

def g(x): return 2*x + 6

def h(x): return  -x

my_functions = (f, g, h)
for function in my_functions:
    print(function(2))
    print(f'{function}({2}) = {function(2)}')


def check_list(a_list):
    if 'hello' in a_list:
        return True

# ***********************************************************
x = 5
def my_f(y):
    print(y)
my_f(8)
print(x)

# ***********************************************************
def outer_function(var1):
    y = 12
    a = var1

def inside_function():
    b = 17
    print(x, y, a, b)
    # print(b)
    inside_function()

# print(y)
outer_function(4)
inside_function()