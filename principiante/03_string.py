### Strings ###
my_string = "Hello, World!"
my_other_string = "Python Programming"

print(len(my_string))
print(len(my_other_string))

print(my_string + " " + my_other_string)  # Concatenación de cadenas

my_new_string = "Este es un String \ncon salto de linea"
print(my_new_string)

my_tabbed_string = "\tEste es un String con tabulación"
print(my_tabbed_string)

my_scaped_string = "Este es un String con comillas dobles \" y comillas simples '"
print(my_scaped_string)

# Formateo de cadenas
name, last_name, age = "Nicolas", "David", 24

print("Mi nombre es {} {} y tengo {} años".format(name, last_name, age))
print("Mi nombre es %s %s y tengo %d años" % (name, last_name, age))
print(f"Mi nombre es {name} {last_name} y tengo {age} años") # f sirve para formatear cadenas e inferir variables


# Desempaquetado de caracteres
language = "Python"
a, b, c, d, e, f = language
print(a, b, d, e, f)


# División de cadenas
language_slice = language[0:3]  # Desde el índice 0 hasta el 3 (sin incluir el 3)
print(language_slice)

language_slice = language[:3]  # Desde el inicio hasta el índice 3
print(language_slice)

language_slice = language[3:]  # Desde el índice 3 hasta el final
print(language_slice)

language_slice = language[-3]  # Desde el índice -3 desde el final
print(language_slice)

reversed_language = language[::-1]  # Invertir la cadena
print(reversed_language)

### Métodos de cadenas ###
print(language.upper())  # Convertir a mayúsculas
print(language.lower())  # Convertir a minúsculas
print(language.capitalize())  # Capitalizar la primera letra
print(language.title())  # Capitalizar la primera letra de cada palabra
print(language.count("o"))  # Contar ocurrencias de un carácter
print(language.find("t"))  # Encontrar el índice de un carácter
print(language.replace("o", "0"))  # Reemplazar un carácter por otro
print(language.startswith("Py"))  # Verificar si comienza con "Py"
print(language.endswith("on"))  # Verificar si termina con "on"
print(language.split("t"))  # Dividir la cadena en una lista por el carácter "t"
print(language.isalpha())  # Verificar si todos los caracteres son alfabéticos
print(language.isdigit())  # Verificar si todos los caracteres son dígitos
print(language.isalnum())  # Verificar si todos los caracteres son alfanuméricos
print(language.strip("P"))  # Eliminar caracteres al inicio y al final
print(language.lstrip("P"))  # Eliminar caracteres al inicio
print(language.rstrip("n"))  # Eliminar caracteres al final
print(language.isnumeric())  # Verificar si todos los caracteres son numéricos
print("1".isnumeric())  # Verificar si "1" es numérico
print(language.upper().isupper())  # Verificar si la cadena en mayúsculas es mayúscula