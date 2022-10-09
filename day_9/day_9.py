# if elif else

# nivel 1
# 1
# edad = int(input('Ingresa tu edad: '))

# if edad >= 18:
#     print('Tienes edad para conducir')
# else:
#     print(f'Te faltan {18 - edad} años para poder conducir')

# 2

# edad = int(input('Ingresa tu edad: '))

# if edad > 25 and (edad - 25) > 1:
#     print(f'Tienes {edad - 25} años mas que yo')
# elif edad > 25 and (edad - 25) == 1:
#     print(f'Tienes un año mas que yo')
# elif edad < 25 and (25 - edad) > 1:
#     print(f'Tienes {25 - edad} años menos que yo')
# elif edad < 25 and (25 - edad) == 1:
#     print(f'Tienes un año menos que yo')
# else:
#     print('Tienes mi misma edad')

# 3

# a = int(input('Ingresa el digito a: '))
# b = int(input('Ingresa el digito b: '))

# if a > b:
#     print('a es mas grande que b')
# elif a < b:
#     print('b es mas grande que a')
# else:
#     print('a y b son iguales')

# nivel 2
# 1

# nota = int(input('Nota: '))

# if nota >= 90 and nota <= 100:
#     print('A')
# elif nota >= 70 and nota <= 89:
#     print('B')
# elif nota >= 60 and nota <= 69:
#     print('C')
# elif nota >= 50 and nota <= 59:
#     print('D')
# else:
#     print('F')

# 2

# mes = input('Mes: ')

# if mes == 'septiembre' or mes == 'octubre' or mes == 'noviembre':
#     print('Estamos en primavera')
# elif mes == 'diciembre' or mes == 'enero' or mes == 'febrero':
#     print('Estamos en verano')
# elif mes == 'junio' or mes == 'julio' or mes == 'agosto':
#     print('estamos en invierno')
# elif mes == 'marzo' or mes == 'abril' or mes == 'mayo':
#     print('estamos en otoño')

# 3

# frutas = ['platano', 'naranja', 'mango', 'limon']

# fruta = input('Ingresa una fruta: ')

# if fruta in frutas:
#     print('Esa fruta ya está en la lista')
# else:
#     frutas.append(fruta)
#     print(frutas)

# 4

person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
        }
    }

if 'skills' in person.keys():
    print(person['skills'][len(person['skills'])//2])
    print(f'python está en la lista de habilidades?: {"Python" in person["skills"]}')
if  'Javascript' in person['skills'] and 'React' in person['skills'] and len(person['skills']) == 2 :
    print('es un desarrollador front-end')
elif  'Node' in person['skills'] and 'Python' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3 :
    print('es un desarrollador back-end')
elif  'Node' in person['skills'] and 'React' in person['skills'] and 'MongoDB' in person['skills'] and len(person['skills']) == 3 :
    print('es un desarrollador Full stack')
else:
    print('ni idea a que se dedica')


