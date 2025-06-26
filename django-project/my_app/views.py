from django.http import HttpResponse

# Este es el archivo que se encarga de procesar las peticiones y devolver las respuestas
# Es el archivo principal de la aplicación

def hello_world(request):
    return HttpResponse("<h1>Hello World</h1>")

def about(request):
    return HttpResponse("<h1>About</h1>")