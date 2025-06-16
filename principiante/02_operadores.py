### Operadores aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(10 % 3)
print(3 / 4)
print(
    10 // 3
)  # División entera para que el resultado sea un entero y tome el valor más bajo
print(2**3)  # Exponente, 2 elevado a la potencia de 3
print(2**3 + 3 - 7 / 1 // 4)

print("Hola" + "Python")  # Concatenación de cadenas
# print("Hola" + 4)  # Esto generará un error porque no se puede concatenar una cadena con un entero
print("Hola" + str(4))  # Esto convierte el entero a cadena antes de concatenar
print("Hola" * 3)  # Repite la cadena "Hola" 3 veces
print("Hola" * (2**3))  # Repite la cadena "Hola" 8 veces (2 elevado a la potencia de 3)
print("Hola" * 0)  # Repite la cadena "Hola" 0 veces, lo que resulta en una cadena vacía

### Operadores de comparación ###
print(3 > 4)  # Mayor que
print(3 < 4)  # Menor que
print(3 >= 4)  # Mayor o igual que
print(3 <= 4)  # Menor o igual que
print(3 == 4)  # Igual que
print(3 != 4)  # Diferente de

print("Hola" > "Python")  # Compara cadenas lexicográficamente
print("Hola" < "Python")  # Compara cadenas lexicográficamente
print("Hola" >= "Python")  # Compara cadenas lexicográficamente
print("Hola" <= "Python")  # Compara cadenas lexicográficamente
print("Hola" == "Python")  # Compara cadenas para igualdad
print("Hola" != "Python")  # Compara cadenas para desigualdad
print("Hola" == "Zola")  # Lo que se esta comparando es una ordenacion alfabética de las letras, no el significado de las palabras ni la cantidad de caracteres
print("aaa" >= "aba")  # Compara cadenas lexicográficamente, "aaa" es menor que "aba"

""" La comapracion de cadenas se realiza de manera lexicográfica, es decir, se compara carácter por carácter según su orden en la tabla ASCII. """

### Operadores lógicos ###
print(3 > 4 and 5 < 6)  # Operador lógico AND
print(3 > 4 or 5 < 6)  # Operador lógico OR
print(not 3 > 4)  # Operador lógico NOT
print(not (3 > 4 and 5 < 6))  # Negación de una expresión lógica
print(3 > 4 and not (5 < 6))  # Combinación de operadores lógicos