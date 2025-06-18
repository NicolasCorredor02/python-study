### BUCLES ###

# While

my_condition = 0

while my_condition < 10:
    print(my_condition)
    my_condition += 1
else:
    print("La condicion es mayor o igual que 10")

print("La ejecucion continua")    


while my_condition <  20:
    my_condition += 1
    if my_condition == 15:
        print("La condicion es 15, se detiene la ejecucion")
        break
    print(my_condition)
    
# For

my_list = [1, 2, 3, 4, 5]

for element in my_list:
    print(f"Valor en lista: {element}")

my_tuple = (24, 1.80, "Nicolas", "David")

for element in my_tuple:
    print(f"Valor en tupla: {element}")

my_set = ("Nicolas", "David", 24, 1.75, True)

for element in my_set:
    print(f"Valor en set: {element}")

my_dict = {
    "name": "Nicolas",
    "last_name": "David",
    "age": 24,
    "heigh": 1.75,
    "is_worker": True,
}

for element in my_dict:
    print(f"Clave en diccionario: {element}")
    print(f"Valor en diccionario: {my_dict[element]}")
    

for element in my_dict:
    print(f"Clave en diccionario: {element}")
    if element == "last_name":
        print(f"Valor en diccionario: {my_dict[element]} - Se detiene la ejecucion")
        break
else:
    print("No hay mas elementos en el diccionario") # A diferencia del while, el else se ejecuta si no se cumple la condicion
    

for element in my_dict:
    print(f"Clave en diccionario: {element}")
    if element == "last_name":
        print(f"Valor en diccionario: {my_dict[element]} - Se detiene la ejecucion")
        continue # A diferencia del break, el continue se ejecuta si se cumple la condicion
else:
    print("No hay mas elementos en el diccionario")
