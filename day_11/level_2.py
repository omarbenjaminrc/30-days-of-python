# Declare a function named evens_and_odds . It takes a positive integer as parameter and it counts number of evens and odds in the number.
from asyncio.windows_events import NULL
import math
 


def evens_and_odds(num):
    par     = 0
    impar   = 0
    for i in range(num+1):
        if i % 2 == 0:
            par += 1
        else:
            impar += 1

    texto = f'numeros pares: {par}\nnumeros impares: {impar}'
    return texto
    
# Call your function factorial, it takes a whole number as a parameter and it return a factorial of the number

def factorial(num):
    return math.factorial(num)

# Call your function is_empty, it takes a parameter and it checks if it is empty or not

def is_empty(x):
    if x == NULL or x == None or x == '' or x == [] or x == {} or x == ():
        return True
    else:
        return False

# Write different functions which take lists. They should calculate_mean, calculate_median, calculate_mode, calculate_range, calculate_variance, calculate_std (standard deviation).

def calculate_mode(lista):
    sorted(lista)
    return lista[len(lista) //2]

def calculate_median(lista):
    total = 0
    for i in lista:
        total += i
    return total / len(lista)

    
