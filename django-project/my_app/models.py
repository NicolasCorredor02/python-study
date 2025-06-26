from django.db import models

# Este archivo se encarga de crear los modelos de la aplicacion
# Los modelos son la representacion de la base de datos
# Los modelos se crean en la base de datos
# Los modelos se crean en la aplicacion
# Los modelos se crean en el archivo models.py
# Los modelos se crean en la base de datos
# Los modelos se crean en la aplicacion
# Los modelos se crean en el archivo models.py
# Los modelos se crean en la base de datos


# Aca se esta creando una tabla llamada Project con la columna name de tipo CharField
class Project(models.Model):
    name = models.CharField(max_length=100)

    # Este metodo se encarga de mostrar el nombre del proyecto en el panel de administracion
    def __str__(self):
        return self.name


class Task(models.Model):

    # Este metodo se encarga de mostrar el nombre de la tarea en el panel de administracion
    def __str__(self):
        return self.title + " - " + self.project.name

    title = models.CharField(max_length=100)
    description = models.TextField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    done = models.BooleanField(default=False)
