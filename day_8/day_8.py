# diccionarios

dog = {}
dog['nombre'] = 'laico'
dog['color'] = 'negro'
dog['raza'] =  'quiltor'
dog['edad'] = 3

student = {
    'first_name': 'Omar', 
    'last_name': 'Ramirez', 
    'gender': 'Male', 
    'age': 23, 
    'marital_status': 'single', 
    'skills': ['Python','SQL','Botstrap','Javascrip'], 
    'country': 'Chile', 
    'city': 'Temuco', 
    'address': 'Bayona 1'
    }

len_student = len(student)
skils = student['skills']
print(type(skils))

skils.append('Mysql')
print(student['skills'])
print(student.keys())
print(student.values())
print(student.items())

del student['age']
print(student)
del student





