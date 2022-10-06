# tuplas

# nivel 1
# 1
tupla_vacia = tuple()
# 2
tupla_hermanos = ('gaby','cristobal')
# 3
familiares = tuple()
mi_familia = familiares + tupla_hermanos
# 4
print(len(mi_familia))
# 5
mi_familia = mi_familia + ('mamá','papá')

# nivel 2
a = list(mi_familia)
frutas      = ('manzanas','peras','platanos','tomates')
vegetales   = ('zanaorias','cebollas','pepinos','papas')
producto_animales = ('queso','leche','carne','cuero')

food_stuff_tp = frutas + vegetales + producto_animales
food_stuff_lt = list(food_stuff_tp)

print(food_stuff_tp[6:])

print(food_stuff_tp[0:3], food_stuff_lt[-3:])

del food_stuff_tp
print(food_stuff_tp)

nordic_countries = ('Denmark', 'Finland','Iceland', 'Norway', 'Sweden')

print('Estonia' in nordic_countries)
print('Iceland' in nordic_countries)





