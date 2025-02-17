# Uncomment the imports below before you add the function code
# import requests
import os
from dotenv import load_dotenv

load_dotenv()

backend_url = os.getenv(
    'backend_url', default="http://localhost:3030")
sentiment_analyzer_url = os.getenv(
    'sentiment_analyzer_url',
    default="http://localhost:5050/")

import requests
from urllib.parse import urlencode

def get_request(endpoint, **kwargs):
    try:
        # Construcción segura de la URL con parámetros
        request_url = f"{backend_url}{endpoint}"
        if kwargs:
            request_url += "?" + urlencode(kwargs)  # Codifica los parámetros correctamente
        
        print(f"GET from {request_url}")

        # Llamada HTTP con manejo de excepciones
        response = requests.get(request_url, params=kwargs, timeout=10)  # Agregar timeout opcional
        response.raise_for_status()  # Lanza error si la respuesta no es 2xx
        
        return response.json()
    
    except requests.exceptions.RequestException as e:
        print(f"Network exception occurred: {e}")
        return None  # Devolver None en caso de error



def analyze_review_sentiments(text):
    request_url = sentiment_analyzer_url+"analyze/"+text
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(request_url)
        return response.json()
    except Exception as err:
        print(f"Unexpected {err=}, {type(err)=}")
        print("Network exception occurred")

def post_review(data_dict):
    request_url = backend_url+"/insert_review"
    try:
        response = requests.post(request_url,json=data_dict)
        print(response.json())
        return response.json()
    except:
        print("Network exception occurred")
