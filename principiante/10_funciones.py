### FUNCIONES ###

def my_funtion ():
    print("My function")

my_funtion()

def sum_two_values (value1: int = 1, value2: int = 1):
    return value1 + value2

result = sum_two_values(10, 20)
print(result)

def print_name (name: str = "John", last_name: str = "Doe"):
    print(f"Your name is {name} {last_name}")
    
print_name("Nicolas", "David")

def print_texts(*text: str): # Aca el * se usa para indicar que se puede pasar cualquier cantidad de argumentos
    print(text)
    print(type(text))


def print_upper_texts(*text: str): 
    for text in text:
        print(text.upper())
    
print_texts("Hello", "World", "Python", "Programming")
print_texts("Hello")

print_upper_texts("Hello", "World", "Python", "Programming")
print_upper_texts("Hello")


## Argumentos por clave ##
def describir_persona(nombre, edad, sexo):
    print(f"El nombre es {nombre}, la edad es {edad} y el sexo es {sexo}")

# describir_persona( "Masculino", "Nicolas", 24 ) ## En este caso se interpretaran los parametros como posicionales
describir_persona(sexo="Masculino", edad=24, nombre="Nicolas") ## En este caso se interpretaran los parametros como nombrados y aunque no esten en el mismo orden




