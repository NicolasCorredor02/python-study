### EXCEPCIONES O MANEJO DE ERRORES ###

print(10 / 0) # Esto genera un error de división

try:
    print(10 / 0) # Esto genera un error de división
except:
    print("Se ha producido un error") # Esto se ejecutara si se produce una excepcion
else:
    print("Todo ha ido bien") # Esto se ejecutara si no se produce ninguna excepcion
finally:
    print("Esto se ejecutara siempre") # Esto se ejecutara si se produce una excepcion o no
    
## Excepciones por tipo ##

try:
    print(10 / 0) # Esto genera un error de división
except ZeroDivisionError: # Error de tipo ZeroDivisionError
    print("No se puede dividir por cero")
except TypeError: # Error de tipo TypeError
    print("No se puede dividir un string con un entero")
except NameError: # Error de tipo NameError
    print("No se puede dividir un string con un entero")
except Exception: # Error de tipo Exception
    print("Se ha producido un error")
except ValueError: # Error de tipo ValueError
    print("No se puede dividir un string con un entero")    
except Exception as error: # Error de tipo Exception
    print("Se ha producido un error:", error)