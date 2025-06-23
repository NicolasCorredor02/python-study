### REQUEST O PETICIONES ###

# Como hacer peticiones a API's con python 

# 1. Sin dependencias

import urllib.request
import json

api_post = "https://jsonplaceholder.typicode.com/posts"

try:
    response = urllib.request.urlopen(api_post) # Es como decirle que vaya a la pagina donde se encuentran los datos pero aun no los trabaje ni traiga
    data = response.read() # Trae los datos de la pagina pero en este punto estan codificados
    json_data = json.loads(data.decode('utf-8')) # Decodifica los datos en json con utf-8

    print(json_data) # Imprime los datos

    response.close() # Cierra la conexion
except Exception as e:
    print(f"Error: {e}")


# 2. Con requests (request)

import requests  # Importa la biblioteca requests


print("\nGET")

api_posts = "https://jsonplaceholder.typicode.com/posts"
response = requests.get(api_posts)
json = response.json()

print(json[0])


import requests  # Importa la biblioteca requests


print("\nPOST")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts/"
    new_post = {
        "title": "Mi nuevo post",
        "body": "Contenido del nuevo post",
        "userId": 1
    }
    response = requests.post(api_posts, json=new_post)
    print (response.json())
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


print("\nPUT")
try:
    api_posts = "https://jsonplaceholder.typicode.com/posts/1"
    new_post = {
        "title": "Mi post actualizado",
        "body": "Contenido del nuevo post actualizado",
        "userId": 2
    }
    response = requests.put(api_posts, json=new_post)
    print (response.json())
except requests.exceptions.RequestException as e:
    print(f"Error en la solicitud: {e}")


 # Usar la API de GPT-4o de Open AI
import os
from dotenv import load_dotenv

# Carga las variables de entorno del archivo .env
load_dotenv()

DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")

def call_deepseek_api(api_key, prompt):
    url = "https://api.deepseek.com/chat/completions"  

    headers = {
    "Content-Type": "application/json",
    "Authorization": f"Bearer {api_key}"
    }

    data = {
    "model": "deepseek-chat",
    "messages": [
        {"role": "user", "content": prompt},
    ],
    "stream": False
    }

    response = requests.post(url, headers=headers, json=data)

    print(response.json())

call_deepseek_api(DEEPSEEK_API_KEY, "Hola, ¿cómo estás?") # Da eror ya que no tengo saldo en la API de DeepSeek