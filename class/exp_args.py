"""
Create a function sum_args that takes any number of arguments and returns their sum.
"""
def sum_args (*x):
    return sum(x)
print(sum_args(1,1,1,1))

"""
Write a function concat_strings that takes any number of string arguments and concatenates them into a single string.
"""
def concat_strings(*x):
    print(''.join(x))

"""
Implement a function calculate_expenses that takes a person's name, their monthly income, 
and variable expenses as positional arguments. Additionally, 
accept any number of keyword arguments representing fixed expenses. 
Calculate and print the remaining balance after deducting all expenses.
"""

def calculate_expenses(name, monthly_income, *expenses, **fixed_expenses):
    total_expenses = sum(expenses)
    total_fixed_expenses = sum(fixed_expenses.values())
    remaining_balance = monthly_income - (total_expenses + total_fixed_expenses)
    print(f' The remaining balance is: {remaining_balance}')

calculate_expenses('Rossy',
                   100000,
                   45, 100, 1500, 45,
                   internet=500, food=1000, coffee=2000, uñas=600, pestañas=500, tinte=500, regalos_monito=800)
# expenses = tupla
# fixed expenses = diccionario

def my_fun(*v1, **v2):
    return v1, v2

my_fun(1, 2, 3, 4, 6, c1='a', c2='b')
print(my_fun)
