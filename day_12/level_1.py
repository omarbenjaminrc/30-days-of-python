import random,string

def random_user_id():
    todo = string.ascii_letters + string.digits
    user_id = ''
    for i in range(6):
        user_id += todo[random.randint(0,len(todo)-1)]
    return user_id

def random_user_id_by_user(ides,caracteres):
    todo = string.ascii_letters + string.digits
    lista = []
    for a in range(ides):
        user_id = ''
        for i in range(caracteres):
            user_id += todo[random.randint(0,len(todo)-1)]
        lista.append(user_id)
        
    return lista

def rgb_color_gen():
    color = []
    for i in range(3):
        color.append(random.randint(0,255))
    return f'rgb({color})'

def hexa_colors():
    lista = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f']
    hexadecimal = ''
    for i in range(6):
        hexadecimal += f'{random.choice(lista)}'
    return '#'+hexadecimal

print(hexa_colors())

