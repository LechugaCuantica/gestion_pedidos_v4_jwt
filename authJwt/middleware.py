from django.http import HttpRequest, JsonResponse
from django.shortcuts import redirect, render
import requests
from requests import exceptions
import dotenv
import os

dotenv.load_dotenv()

URL = os.getenv('API_URL')

class AuthMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request: HttpRequest):
        try:
            # Solo en las rutas que inicien en dashboard
            if request.path.startswith("/dashboard/"):
                # Obtenemos el token
                token = request.COOKIES.get('token')
                # Si existe el token 
                if token:
                    # Hacemos la petición
                    response = requests.get(f"{URL}/auth", cookies={'token': token})
                    # Si la respuesta es correcta cargamos la vista de la ruta
                    if response.status_code == 200:
                        return self.get_response(request)
                    else:
                        redirect("/?error=No se ha podido autenticar la sesión, inicie sesión nuevamente.")
                
                # De lo contrario redireccionamos al login
                return redirect("/")
            
            return self.get_response(request)
        except exceptions.ConnectionError:
            return render(request, "error.html", {'status_code': 503, 'title': 'Error 503 - Servicio no disponible', 'description': 'Error de conexión con el servicio de autenticación. Intente mas tarde.'})



        