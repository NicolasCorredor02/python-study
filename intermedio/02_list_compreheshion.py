### LIST COMPREHENSION ###

# Las listas comprimidas son una forma de crear una nueva lista basada en una lista existente
my_list = [32, 123, 22, 12, 34, 45, 65, 87, 19, 81]
squared_list = [x**2 for x in my_list] # x es el elemento de la lista my_list y se eleva al cuadrado y se agrega a la lista squared_list

print(squared_list)

# Otro ejemplo
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
even_numbers = [i for i in range(81)] # range(8) genera la lista [0, 1, 2, 3, 4, 5, 6, 7]
print(even_numbers)

# otro uso mas avanzado
my_list = [0, 1, 2, 3, 4, 5, 6, 7]
even_numbers = [i for i in range(101) if i % 2 == 0] # Crea un rango de 0 a 100 y filtra los números pares 
print(even_numbers)

