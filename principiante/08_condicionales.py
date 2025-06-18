### CONDICIONALES ###

my_condition = False

if my_condition:
    print("The condition is True")


my_condition = 5 * 5

if my_condition == 10:
    print("The condition is True")

if my_condition > 10 and my_condition < 20:
    print("Es mayor que 10 y menor que 20")
elif my_condition == 25:
    print("Es igual a 25")
else:
    print("Es menor o igual que 10 o mayor o igual que 20 o distinto a 25")
    

my_string = ""

if not my_string:
    print("The string is empty")
else:
    print("The string is not empty")