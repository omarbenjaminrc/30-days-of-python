from ast import Delete

# nivel 1
lista = list()
lista2 = [1,2,3,4,5,6,7]
print(len(lista2))
print(f'{lista2[0]},{lista2[3]},{lista2[-1]}')
mixed_data_types = ['Omar',23,1.75,'soltero','bayona 1 1941']
it_companies = ['facebook','google','microsoft','apple','ibm','oracle','amazon']
print(it_companies)
print(len(it_companies))
print(it_companies[0],it_companies[3],it_companies[-1])
it_companies[0] = 'Facebook'
print(it_companies)
it_companies.append('ntt data')
it_companies.insert(4,'OpenIA')
it_companies[1] = it_companies[1].upper()
print(it_companies)
it_companies.append('#; ')
print( 'ibm' in it_companies)
it_companies.sort()
it_companies.reverse()
print(it_companies)
print(it_companies[0:3])
print(it_companies[-3:])
print(it_companies[3:6])
print(it_companies.pop(0))
print(it_companies.pop(-1))
print(it_companies.pop(3))
print(it_companies.clear())
del it_companies
front_end,back_end =['HTML', 'CSS', 'JS', 'React', 'Redux'],['Node','Express', 'MongoDB']
full_stack = front_end + back_end
full_stack.insert(5,'Python')
full_stack.insert(6,'SQL')
print(full_stack)

# nivel 2

ages = [19, 22, 19, 24, 20, 25, 26, 24, 25, 24]
ages.sort()
print(f'min = {min(ages)}, max = {max(ages)}')
ages.insert(0,18)
ages.append(27)
print(ages)
print(sum(ages)/len(ages))
print(f'min = {min(ages)}, max = {max(ages)}')
promedio = sum(ages)/len(ages)
print(abs((min(ages)-promedio)==abs(max(ages)-promedio)))

paises = ['China', 'Russia', 'USA', 'Finland', 'Sweden', 'Norway', 'Denmark']
print(paises[int(len(paises)/2)])

paises1,paises2 = paises[0:3],paises[3:]

print(paises1)
print(paises2)

china,rusia,eeuu,*escandinavia = paises



