# Variables

# La buena practica es nombrar las variables en minúsculas y en foramto snake_case

my_strign_variable = "Variable de String"  # Variable de tipo cadena
print(my_strign_variable)  # Imprime el valor de la variable

my_int_variable = 43  # Variable de tipo entero
print(my_int_variable)  # Imprime el valor de la variable

my_int_to_str_variable = str(my_int_variable)  # Convierte el entero a cadena
print(my_int_to_str_variable)
print(type(my_int_to_str_variable))  # Imprime el tipo de dato de la variable convertida

my_bool_variable = True  # Variable de tipo booleano
print(my_bool_variable)  # Imprime el valor de la variable

# Concatenación de variables
print(
    my_strign_variable, my_int_to_str_variable, my_bool_variable
)  # Imprime los valores de las variables en una sola línea

print(
    "El tamano de la cadena  (my_string_variable) es:", len(my_strign_variable)
)  # Imprime la longitud de la cadena

# Variables en una sola linea
# Aunque se pueden crear varias variables en una sola línea, es recomendable hacerlo solo si las variables son del mismo tipo y tienen un significado similar.
# ! Cuidado con usar esta técnica para variables de diferentes tipos, ya que puede dificultar la lectura del código y la futura depuración.
name, surname, alias, age = (
    "John",
    "Doe",
    "johndoe",
    30,
)  # Asignación múltiple de variables

print("Me llamo:", name, surname, "Mi alias es:", alias, "Mi edad es:", age)


# Uso de inputs para capturar datos del usuario
user_name = input("¿Cual es tu nombre? ")  # Captura el nombre del usuario
print("Hola,", user_name)  # Imprime un saludo con el nombre del usuario

# Tipado debil de los datos
address: str = "Calle Falsa 123"  # Declaración de variable con tipo explícito
address = (
    123  # Esto generará un error si se intenta usar address como cadena más adelante
)
# Aunque se ha declarado como cadena, se le asigna un entero, pero esto aun deja ejecutar el código sin errores de sintaxis.
# Esto se debe a que Python es un lenguaje de tipado dinámico, lo que significa que las variables pueden cambiar de tipo en tiempo de ejecución.
print(
    type(address)
)  # Imprime la dirección, pero puede causar problemas si se usa como cadena más adelante
