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





