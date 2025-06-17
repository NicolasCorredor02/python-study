### Sets ###

# Los sets son colecciones desordenadas de elementos unicos que pueden ser mutables o inmutables dependiendo de la implementación

my_set = set()
my_other_set = {"Nicolas", "David", 24, 1.75, True}

my_other_set.add("Rodriguez")
print(my_other_set)

# 1. Un set no es una estructura ordenada
# 2. Un set no admite datos repetidos

my_other_set.add("Rodriguez")
print(my_other_set)

print("Nicolas" in my_other_set) # True
print("Rodrigouez" in my_other_set) # False


# Eliminar un elemento de un set
my_other_set.remove("Nicolas")
print(my_other_set)

# Limpiar un set
my_other_set.clear()
print(len(my_other_set))

# Eliminar un set completo
del my_other_set

my_set = {"Django", "SpringBoot", ".Net", "Flask", "NestJS"}
my_other_set = {"python", "java", "c", "c++", "c#"}

my_new_set = my_set.union(my_other_set)
print(my_new_set)

print(my_new_set.difference(my_set))
print(my_new_set.difference(my_other_set))