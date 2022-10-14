# names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']. Unpack the first five countries and store them in a variable nordic_countries, store Estonia and Russia in es, and ru respectively.

names = ['Finland', 'Sweden', 'Norway','Denmark','Iceland', 'Estonia','Russia']
*nordic_countries,es,ru = names
print(nordic_countries,es,ru)

for index , pais in enumerate(names):
    print(index,pais)

lista_ordenada  = [1,2,3,4,5,6,7,8,9]
lista_invertida = [9,8,7,6,5,4,3,2,1]

for a,b in zip(lista_ordenada,lista_invertida):
    print(a+b)