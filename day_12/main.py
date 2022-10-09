import mi_modulo
import  math, datetime, os,sys, random, statistics, collections, json,re,string

# nombre = mi_modulo.generar_nombre_completo('Omar','Ramirez')
# print(nombre)

# os

# os.chdir('day_1')
# # os.mkdir('carpeta_001')
# direccion = os.getcwd()
# print(direccion)
# os.rmdir('carpeta_001')

# sys
# print(sys.maxsize)

# statistics

ages = [20, 20, 4, 24, 25, 22, 26, 20, 23, 22, 26]
print(statistics.mean(ages))       # ~22.9
print(statistics.median(ages))     # 23
print(statistics.mode(ages))       # 20
print(statistics.stdev(ages))      # ~2.3


print(math.pi)           # 3.141592653589793, pi constant
print(math.sqrt(2))      # 1.4142135623730951, square root
print(math.pow(2, 3))    # 8.0, exponential function
print(math.floor(9.81))  # 9, rounding to the lowest
print(math.ceil(9.81))   # 10, rounding to the highest
print(math.log10(100))   # 2, logarithm with 10 as base
