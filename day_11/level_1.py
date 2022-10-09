# Declare a function add_two_numbers. It takes two parameters and it returns a sum.

def add_two_numbers(a, b):
    return a + b

# Area of a circle is calculated as follows: area = π x r x r. Write a function that calculates area_of_circle.

def area_of_circle(radio):
    pi = 3.14
    area = pi *radio **2
    return area

# Write a function called add_all_nums which takes arbitrary number of arguments and sums all the arguments. Check if all the list items are number types. If not do give a reasonable feedback.

def add_all_nums(*nums):
    total = 0
    for numero in nums:
        if type(numero) == str:
            return 'no es sumable'
        else:
            total += numero
    return total

# Temperature in °C can be converted to °F using this formula: °F = (°C x 9/5) + 32. Write a function which converts °C to °F, convert_celsius_to-fahrenheit.

def celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * (9/5)) + 32
    return fahrenheit

# Write a function called check-season, it takes a month parameter and returns the season: Autumn, Winter, Spring or Summer.

def check_season(mes):
    
    if mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
        estacion = 'primavera'
    elif mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
        estacion = 'verano'
    elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
        estacion = 'invierno'
    elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
        estacion = 'otoño'
    
    return estacion

# Write a function called calculate_slope which return the slope of a linear equation

def calculate_slope(a,b):
    return (a[1]-b[1]) / (a[0]-b[0])

# Quadratic equation is calculated as follows: ax² + bx + c = 0. Write a function which calculates solution set of a quadratic equation, solve_quadratic_eqn.

def solve_quadratic_eqn(a,b,c,x):
    resultado = a*x**2 + b*x + c
    return resultado

# Declare a function named print_list. It takes a list as a parameter and it prints out each element of the list.

def print_list(lista):
    for item in lista:
        print(item)

# Declare a function named reverse_list. It takes an array as a parameter and it returns the reverse of the array (use loops).

def reverse_list(lista):
    return lista[::-1]


# Declare a function named capitalize_list_items. It takes a list as a parameter and it returns a capitalized list of items

def capitalize_list_items(lista):
    nueva_lista = []
    for item in lista:
        nueva_lista.append(item.capitalize())
    return nueva_lista

# Declare a function named add_item. It takes a list and an item parameters. It returns a list with the item added at the end.

def add_item(list, item):
    return list + [item]

# Declare a function named remove_item. It takes a list and an item parameters. It returns a list with the item removed from it.

def remove_item(lista, item):
    nueva_lista = lista.pop(item)
    return nueva_lista

# Declare a function named sum_of_numbers. It takes a number parameter and it adds all the numbers in that range.

def sum_of_numbers(num):
    n = 0
    for i in range(num+1):
        n += num
    return n

# Declare a function named sum_of_odds. It takes a number parameter and it adds all the odd numbers in that range.

def sum_of_odds(num):
    n = 0
    for i in range(1,(num+1),2):
        n += num
    return n
# Declare a function named sum_of_even. It takes a number parameter and it adds all the even numbers in that - range.

def sum_of_odds(num):
    n = 0
    for i in range(0,(num+1),2):
        n += num
    return n