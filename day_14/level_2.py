from functools import reduce


countries = ['Estonia', 'Finland', 'Sweden', 'Denmark', 'Norway', 'Iceland']
names = ['Asabeneh', 'Lidiya', 'Ermias', 'Abraham']
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]


# Use map to create a new list by changing each country to uppercase in the countries list.

countries_upper = list(map(lambda country : country.upper(), countries))
# print(countries_upper)

# Use map to create a new list by changing each number to its square in the numbers list.

numbers_square = list(map(lambda x : x**x, numbers))
# print(numbers_square)

# Use map to change each name to uppercase in the names list.

names = list(map(lambda x : x.upper(),names))
# print(names)

# Use filter to filter out countries containing 'land'.

def filtro(pais):
    if 'land' in pais:
        return True
    else:
        return False
countries_filter = list(filter( filtro , countries ))
# print(countries_filter)

# Use filter to filter out countries having exactly six characters.

countries_6 = list(filter(lambda x: len(x) is 6, countries))
# print(countries_6)

# Use filter to filter out countries containing six letters and more in the country list.

countries_out_6_plus = list(filter(lambda x : len(x) < 6, countries))
# print(countries_out_6_plus)

# Use filter to filter out countries starting with an 'E'.

countries_out_e = list(filter(lambda x : 'E' not in x , countries))
# print(countries_out_e)

# Chain two or more list iterators (eg. arr.map(callback).filter(callback).reduce(callback)).

listas = map(lambda x : x.upper() ,filter(lambda x : 'E' not in x , countries))
# print(list(listas))

# Declare a function called get_string_lists which takes a list as a parameter and then returns a list containing only string items.

def devolver_string(lista):
    lista2 = [ f'{palabra}' for palabra in lista]
    return lista2

def get_string_lists(listas):
    return reduce( devolver_string, listas)

print(list(get_string_lists()))



















# Use reduce to sum all the numbers in the numbers list.



# Use reduce to concatenate all the countries and to produce this sentence: Estonia, Finland, Sweden, Denmark, Norway, and Iceland are north European countries
# Declare a function called categorize_countries that returns a list of countries with some common pattern (you can find the countries list in this repository as countries.js(eg 'land', 'ia', 'island', 'stan')).



# Create a function returning a dictionary, where keys stand for starting letters of countries and values are the number of country names starting with that letter.



# Declare a get_first_ten_countries function - it returns a list of first ten countries from the countries.js list in the data folder.



# Declare a get_last_ten_countries function that returns the last ten countries in the countries list.


