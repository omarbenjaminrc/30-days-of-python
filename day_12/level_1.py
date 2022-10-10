import random,string

def generar_nombre_completo(primer_nombre,apellido):
    return f' {primer_nombre} {apellido} '

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