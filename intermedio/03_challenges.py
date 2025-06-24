### Chanllenges ###

"""
Ejercicio 1

FIIZ BUZZ

Escribir un programa que muestre por consola (con un print) los números de 1 a 100 (ambos incluidos y con un salto de línea entre cada impresión), sustituyendo los siguientes:
- Múltiplos de 3 por la palabra "fizz".
- Múltiplos de 5 por la palabra "buzz".
- Múltiplos de 3 y de 5 a la vez por la palabra "fizzbuzz".
"""


from ast import For
from operator import le


def fizzbuzz():
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            print("fizzbuzz")
        elif i % 3 == 0:
            print("fizz")
        elif i % 5 == 0:
            print("buzz")
        else:
            print(i)


fizzbuzz()

"""
Ejercicio 2

/*
 * Escribe una función que reciba dos palabras (String) y retorne
 * verdadero o falso (Bool) según sean o no anagramas.
 * - Un Anagrama consiste en formar una palabra reordenando TODAS
 *   las letras de otra palabra inicial.
 * - NO hace falta comprobar que ambas palabras existan.
 * - Dos palabras exactamente iguales no son anagrama.
 */
"""


def is_anagram(word1, word2):
    if word1.lower() == word2.lower():
        return False
        # return list(word1.lower()).sort() == list(word2.lower()).sort()

    return sorted(word1.lower()) == sorted(word2.lower())


print(is_anagram("amor", "roma"))


""" 
Ejercicio 3

/*
 * Escribe un programa que imprima los 50 primeros números de la sucesión
 * de Fibonacci empezando en 0.
 * - La serie Fibonacci se compone por una sucesión de números en
 *   la que el siguiente siempre es la suma de los dos anteriores.
 *   0, 1, 1, 2, 3, 5, 8, 13...
 */
"""

# fibonacci = [0, 1]


def fibonacci_serie(limit):
    serie = [0, 1]

    for i in range(1, (limit + 1) - len(serie)):
        serie.append(serie[i - 1] + serie[i])

    print(serie)
    print(len(serie))


fibonacci_serie(50)


"""
Ejercicio 4
/*
 * Escribe un programa que se encargue de comprobar si un número es o no primo.
 * Hecho esto, imprime los números primos entre 1 y 100.
 */
"""


def is_prime(number):

    is_divisible = False

    for i in range(2, number):
        if number % i == 0:
            is_divisible = True
            break

    if not (is_divisible):
        print(number)


def find_primes(limit):

    for i in range(1, limit + 1):
        is_prime(i)


find_primes(100)

"""
Ejercicio 5

/*
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
 */
"""


def revert_string(string):
    for i in range(len(string) - 1, -1, -1):
        print(string[i], end="")


revert_string("Hola mundo!")
