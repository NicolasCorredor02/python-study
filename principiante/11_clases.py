### CLASES ###


class Person:

    # Constructor de la clase: __init__ es un metodo especial que se llama cuando se crea una instancia de la clase
    def __init__(self, name, last_name, age, heigh):
        self.name = name
        self.last_name = last_name
        self.age = age
        self.heigh = heigh
        self.all_data = dict(name=name, last_name=last_name, age=age, heigh=heigh)
        self.__private_data = "Esta variable es privada" # Se utiliza para indicar que la variable es privada y no se puede acceder desde fuera de la clase
        # pass # Se utiliza para indicar que la clase no tiene implementación

    def saludar(self):
        print(
            f"Hola, soy {self.name} {self.last_name} y tengo {self.age} años y mido {self.heigh} cm"
        )

    def see_all_data(self):
        print(self.all_data)

    def born_year(self, year):

        if year <= 0:
            raise ValueError("El año no puede ser negativo o cero")

        return year - self.age


new_person = Person("Nicolas", "Rodriguez", 24, 1.70)
new_person.saludar()

new_person.see_all_data()

born_year_new_person = new_person.born_year(2025)

print(born_year_new_person)

print(new_person.__private_data)