### Diccionarios ###

# Los diccionarios son colecciones desordenadas de pares clave-valor que pueden ser mutables o inmutables dependiendo de la implementación

my_dict = dict()
my_other_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    1: "Python",  # Se puede usar cualquier tipo de dato como clave
}

my_dict = {
    "name": "John",
    "age": 30,
    "city": "New York",
    "languages": {"Python", "Java", "C++"},
    1: 1.77,
}

print(my_dict)
print(my_other_dict)

print(len(my_dict))
print(len(my_other_dict))

# Acceder a un elemento de un diccionario
print(my_dict["name"])  # John
print(my_dict["age"])  # 30
print(my_dict["city"])  # New York
print(my_dict["languages"])  # {'Python', 'Java', 'C++'}
print(my_dict[1])  # 1.77

# Modificar un elemento de un diccionario
my_dict["name"] = "Nicolas"
print(my_dict["name"])  # Nicolas

# Agregar un elemento al diccionario
my_dict["last_name"] = "Corredor"
print(my_dict["last_name"])  # Corredor

# Eliminar un elemento de un diccionario
del my_dict["name"]
print(my_dict)

# La busqueda se hace por medio del la clave y no el valor
print("name" in my_dict)  # False
print("name" not in my_dict)  # True

print(my_dict.items())  # Retorna una lista de tuplas con los pares clave-valor
print(my_dict.keys())  # Retorna una lista con las claves del diccionario
print(my_dict.values())  # Retorna una lista con los valores del diccionario
print(my_dict.fromkeys(("name", 1)))  # Retorna un diccionario con las claves indicadas

my_new_dict = my_dict.fromkeys(
    ("name", 1)
)  # Se crea un diccionario nuevo con las claves indicadas pero sin valores
print(my_new_dict)

my_list = ["name", 1]
my_new_dict = my_dict.fromkeys(my_list) # Tambien se puede crear un diccionario con las claves de una lista
print(my_new_dict)

# Un uso mas normal es crear un diccionario vacio, solo con claves a partir de un diccionario ya existente
my_new_dict = dict.fromkeys(my_dict)
print(my_new_dict) # {'name': None, 'age': None, 'city': None, 'languages': None, 1: None, 'last_name': None}

my_new_dict = dict.fromkeys(my_dict, ("Valor", "Para todos")) # Se puede asignar un valor a todas las claves
print(my_new_dict)