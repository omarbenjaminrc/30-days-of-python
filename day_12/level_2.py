# Write a function list_of_hexa_colors which returns any number of hexadecimal colors in an array (six hexadecimal numbers written after #. Hexadecimal numeral system is made out of 16 symbols, 0-9 and first 6 letters of the alphabet, a-f. Check the task 6 for output examples).

import random

def hexa_colors(numero):
    hexa_lista = []
    lista = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    for i in range(numero):
        hexadecimal = ''
        for i in range(6):
            hexadecimal += f'{random.choice(lista)}'
        hexa_lista.append('#'+hexadecimal)
    return hexa_lista

# Write a function list_of_rgb_colors which returns any number of RGB colors in an array.

def rgb_colors(num):
    lista_color = []
    for i in range(num):
        color = []
        for i in range(3):
            color.append(random.randint(0,255))
        lista_color.append(f'rgb({str(color)})')
    return lista_color


# Write a function generate_colors which can generate any number of hexa or rgb colors.

def generate_colors(hexa_rgb,cantidad):
    if hexa_rgb == 'hexa':
        return hexa_colors(cantidad)
    else:
        return rgb_colors(cantidad)






