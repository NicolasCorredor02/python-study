### LAMBDAS ####

# Lambda es una función anonima que se usa para crear funciones en una sola linea
# Lambda se usa cuando se necesita crear una función muy corta y simple

sum_two_values = lambda first_value, second_value: first_value + second_value


print(sum_two_values(1, 2))


multiply_values = lambda first_value, second_value: first_value * second_value - 2
print(multiply_values(2, 3))


def sum_three_values(value):
    return lambda firsrt_value, second_value: firsrt_value + second_value + value


print(sum_three_values(3)(1, 2)) # Los parametros de la segunda lambda se pasan como argumentos