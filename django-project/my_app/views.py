from django.http import HttpResponse
from .models import Project, Task
from django.shortcuts import get_object_or_404, render, redirect, get_list_or_404
from .forms import CreateNewTask

# Este es el archivo que se encarga de procesar las peticiones y devolver las respuestas
# Es el archivo principal de la aplicación


def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def hello(request, username):
    return HttpResponse("<h1>Hello %s</h1>" % username)


def projects(request):
    # projects = list(Project.objects.values())
    projects = get_list_or_404(
        Project
    )  # Esta es la forma de obtener todos los proyectos
    return render(request, "projects.html", {"projects": projects})


def tasks(request):
    # task = get_object_or_404(Task, title=title) # Esta es la forma de obtener una tarea especifica

    tasks = get_list_or_404(Task)  # Esta es la forma de obtener todas las tareas
    return render(request, "tasks.html", {"tasks": tasks})


def create_task(request):

    if request.method == "GET":
        return render(request, "create_task.html", {"form": CreateNewTask()})
    else:

        Task.objects.create(
            title=request.POST["title"],
            description=request.POST["description"],
            project_id=request.POST["project"],
        )
        return redirect("tasks")
