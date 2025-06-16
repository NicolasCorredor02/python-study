### Tuples ###

my_tuple = tuple()
my_other_tuple = (1, 2, 3, 4, 5)
print(my_other_tuple)  # (1, 2, 3, 4, 5)

my_tuple = ("Nicolas", "David", 24, 1.75, True)
print(my_tuple)  # ('Nicolas', 'David', 24, 1.75, True)

print(my_tuple[0])  # Nicolas
print(my_tuple[1])  # David

my_tuple.count("Nicolas")# 1
my_tuple.index(1.75)  # 3

""" Las tuplas son inmutables, es decir, no se pueden modificar una vez creadas."""

my_sum_tuple = my_other_tuple + my_tuple

print(my_sum_tuple)  # (1, 2, 3, 4, 5, 'Nicolas', 'David', 24, 1.75, True)

print(my_sum_tuple[3:6]) # (4, 5, 'Nicolas')

# Para hacer mutable una tupla, se puede convertir a lista y luego de modificarla, volver a convertirla a tupla.
my_list = list(my_sum_tuple)
my_list[0] = "Modified"
print(type(my_list))  # <class 'list'>
print(my_list)  # ['Modified', 2, 3, 4, 5, 'Nicolas', 'David', 24, 1.75, True]

# En el caso de que se quiera volver a convertir a tupla:
my_sum_tuple = tuple(my_list)
print(type(my_sum_tuple))  # <class 'tuple'>
print(my_sum_tuple)  # ('Modified', 2, 3, 4, 5, 'Nicolas', 'David', 24, 1.75, True)

# Tuplas anidadas
my_nested_tuple = (1, 2, (3, 4, 5), 6)
print(my_nested_tuple)  # (1, 2, (3, 4, 5), 6)
print(my_nested_tuple[2])  # (3, 4, 5)
print(my_nested_tuple[2][1])  # 4

# Desempaquetado de tuplas
a, b, c, d = my_other_tuple
print(a)  # 1
print(b)  # 2
print(c)  # 3

# Borrado de tuplas
del my_tuple
# print(my_tuple)  # NameError: name 'my_tuple' is not defined

# Borrado de un elemento de una tupla no es posible, ya que son inmutables.
del my_tuple[0]  # TypeError: 'tuple' object doesn't support item deletion