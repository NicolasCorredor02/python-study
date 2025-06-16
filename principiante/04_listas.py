### Listas ###

my_list = list()
my_other_list = [1, 2, 3, 4, 5]
print(my_other_list)
print(len(my_other_list))

my_data_list = ["Nicolas", "David", 24, 1.75, True]
print(my_data_list)

print(my_data_list[0])  # Nicolas
print(my_data_list[1])  # David
print(my_data_list[2])  # 24
print(my_data_list[3])  # 1.75
print(my_data_list[4])  # True

# count cuenta el número de veces que aparece un elemento en la lista
print(my_data_list.count("Nicolas"))  # 1

# Aca se esta destructurando la lista
# Es necesario destructurar todos los elementos de la lista, ya que, de lo contrario, no se puede acceder a los elementos de la lista
name, last_name, age, heigh, is_worker = my_data_list
print(name)       # Nicolas
print(last_name)  # David
print(age)        # 24

# Si no se quiere destructurar todos los elementos de la lista, se puede hacer de la siguiente manera
last_name = my_data_list[1]
print(last_name)  # David


print(my_other_list + my_data_list)  # [1, 2, 3, 4, 5, 'Nicolas', 'David', 24, 1.75, True]


# Mutabilidad de las listas
my_other_list.append(6)  # Agrega un elemento al final de la lista
print(my_other_list)  # [1, 2, 3, 4, 5, 6]

my_other_list.insert(3, 56)  # Agrega un elemento en el indice indicado en este caso el inidice es el 3 y el valor es 56
print(my_other_list)  # [1, 2, 3, 56, 4, 5, 6]

# En el caso de que se encuentren varios elementos con el mismo valor, se elimina el elemento en el primer indice que se encuentre
my_other_list.remove(56)  # Elimina el elemento indicado
print(my_other_list)  # [1, 2, 3, 4, 5, 6]

# Elimina el ultimo elemento de la lista y lo devuelve
print(my_other_list.pop())  # 6
print(my_other_list)  # [1, 2, 3, 4, 5]
# Tambien se puede eliminar un elemento en un indice especifico
print(my_other_list.pop(2))  # 3
print(my_other_list)  # [1, 2, 4, 5]

# Se puede eliminar un elemento en un indice especifico y no devolverlo
del my_other_list[2]  # Elimina el elemento en el indice indicado
print(my_other_list)  # [1, 2, 5]

# Se puede ordenar una lista de manera ascendente
my_other_list.sort()  # Ordena la lista de manera ascendente
print(my_other_list)  # [1, 2, 5]

# Se puede ordenar una lista de manera descendente
my_other_list.sort(reverse=True)  # Ordena la lista de manera descendente
print(my_other_list)  # [5, 2, 1]

# Se puede invertir el orden de los elementos de la lista
my_other_list.reverse()  # Invierte el orden de los elementos de la lista
print(my_other_list)  # [1, 2, 5]

# Se puede limpiar la lista
my_other_list.clear()  # Limpia la lista
print(my_other_list)  # []

# Se puede crear una lista con un rango de numeros
my_range_list = list(range(10))  # Crea una lista con un rango de numeros del 0 al 9
print(my_range_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Se puede crear una lista con un rango de numeros y un paso
my_range_list_step = list(range(0, 10, 2))  # Crea una lista con un rango de numeros del 0 al 9 con un paso de 2
print(my_range_list_step)  # [0, 2, 4, 6, 8]

my_new_range_list = my_range_list.copy()  # Crea una copia de la lista
print(my_new_range_list)  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

sub_list = my_new_range_list[2:5]  # Crea una sublista desde el indice 2 hasta el 5 (sin incluir el 5)
print(sub_list)  # [2, 3, 4]