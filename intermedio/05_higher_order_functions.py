### Higher Order Fucntions ###


from functools import reduce


def sum_one(value):
    return value + 1


def sum_five(value):
    return value + 5


def sum_two_values_and_add_something(first_value, second_value, f_sum):
    return f_sum(first_value + second_value)


print(sum_two_values_and_add_something(5, 2, sum_one))
print(sum_two_values_and_add_something(5, 2, sum_five))

### Closures ###


# Esta funcion es un closure porque retorna otra funcion
def sum_ten(original_value):
    def add(value):
        def sum(value2):
            return value + value2 + original_value

        return sum

    return add


add_closure = sum_ten(1)


# print(add_closure(5))

print(sum_ten(1)(5)(2))


### Built-in Higher Order Functions ###

numbers = [2, 5, 10, 21, 31, 3]


# MAP
# El MAP recorre todos los elementos de una lista y ejecuta una funcion en cada uno
def multiply_by_two(item):
    return item * 2


# result = list(map(multiply_by_two, numbers))
result = list(map(lambda item: item * 2, numbers))


print(result)


# FILTER
#  El FILTER recorre todos los elementos de una lista y ejecuta una funcion en cada uno para validar si el elemento cumple con la condicion retornando True o False en base a la condicion, y de acuerdo a esta condicion se agrega o no el elemento a la nueva lista


def filter_greater_than_ten(numer):
    return numer > 10


# result = list(filter(filter_greater_than_ten, numbers))

result = list(filter(lambda item: item > 10, numbers))
print(result)


# REDUCE
# El REDUCE recorre todos los elementos de una lista y ejecuta una funcion en cada uno para obtener un resultado final, lo que hace es operar los elementos de la lista hasta obtener un resultado final mientras que almacena los valores de cada iteracion tanto el elemento anterior como el actual

# Opera un valor mas el acumulado


def sum_two_values(first_value, second_value):
    print(f"first_value: {first_value}, second_value: {second_value}")
    return first_value + second_value


result = reduce(sum_two_values, numbers)


print(result)
