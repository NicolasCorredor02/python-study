### MODULOS ###

# import my_module
from my_module import sum_two_values, print_name

# from 10_funciones import print_name # Aca da error ya que los modulos no pueden tener un nombre que empiece con un numero

# sum_two_values = my_module.sum_two_values(3,5)
sum_two_values = sum_two_values(3,5)
print(sum_two_values)

print_name("Nicolas", "David")

import math

print(math.pi) # Pi
print(math.pow(2,3)) # Potencia
print(math.sqrt(9)) # Raiz cuadrada
print(math.floor(2.5)) # Redondea hacia abajo
print(math.ceil(2.5)) # Redondea hacia arriba

from math import pi as num_pi

print(num_pi)