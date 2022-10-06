# sets
# level 1
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]

print(len(it_companies))
it_companies.add('Twitter')
print(it_companies)
it_companies.update(['HP','Dell','Asus','NTT Data'])
print(it_companies)
it_companies.discard('NTT Data')
print(it_companies)
print('the diference between remuve and discard is than if the given value is not in the set discard don\'t rice any error ')

# level 2

C = A.union(B)
print(A.intersection(B))
print(A.issubset(B))
print(A.isdisjoint(B))
A.union(B)
B.union(A)
print(A.symmetric_difference(B))

del A,B,C

# Level 3

set_ages = set(age)
print(f'the list age length is: {len(age)}\nthe set age length is: {len(set_ages)}')

print('\nthe diference between string, list, tuple and set\nString: is a grup of chars\nList: is iterable chain of any data kind\nTuple: like a list but you can\'t change any data on it\nSet: is a unorder group of data than is unique\n ')

frase = 'I am a teacher and I love to inspire and teach people'
frase = frase.split()
frese = set(frase)
print(len(frase))





