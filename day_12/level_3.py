# Call your function shuffle_list, it takes a list as a parameter and it returns a shuffled list
import random
def shuffle_list(lista):
    random.shuffle(lista)
    return lista 
    
# Write a function which returns an array of seven random numbers in a range of 0-9. All the numbers must be unique.
def unique():
    lista = []
    while len(lista) < 7 :
        lista.append(random.randint(0,9))
        lista = list(set(lista))
    return lista

print(unique())