from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("about/", views.about, name="about"),
    path("hello/<str:username>/", views.hello, name="hello"),
    path("projects/", views.projects, name="projects"),
    path("view_all_tasks/", views.tasks, name="tasks"),
    path("addtask/", views.create_task, name="create_task"),
]
