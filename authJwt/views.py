from os import error

from django.http import HttpRequest
from django.shortcuts import redirect, render
import requests
from requests import exceptions
from authJwt.forms import LoginForm

# Create your views here.
def login(request: HttpRequest):
    try: 
        if (request.method == 'POST'):
            form = LoginForm(request.POST)
            if (form.is_valid()):
                # URL del la api
                url = 'http://127.0.0.1:4000/login'
                # Hacemos la petición con la cookies de la app
                response = requests.post(url, data=form.cleaned_data, cookies=request.COOKIES)
                if response.status_code == 200:
                    # Si es correcto el seteamos el token el las cookies de la app
                    django_response = redirect('dashboard')
                    django_response.set_cookie('token', response.cookies.get('token'))
                    return django_response
                else:
                    # De lo contrario mandamos el error
                    return render(request, 'authJwt/login.html', {'form': form, 'error': response.json()})            
        else:
            form = LoginForm()
            # Obtenemos el token de la cookie
            token = request.COOKIES.get('token')
            # Si existe el token
            if token:
                url = 'http://127.0.0.1:4000/auth'
                # Hacemos la petición para verificar si es válido
                response = requests.get(url, cookies={'token': token})
                
                # Si es correcta redireccionamos al dashboard sin necesidad del login
                if response.status_code == 200:
                    return redirect('dashboard')
                
            #  De lo contrario cargamos el formulario
            if request.GET.get('error'):
                return render(request, 'authJwt/login.html', {'form': form, 'error': {'detail': {'message': request.GET.get('error')}}})
            
            return render(request, 'authJwt/login.html', {'form': form})
    except exceptions.ConnectionError:
        return render(request, 'authJwt/login.html', {'form': form, 'error': {"detail": {"message": 'Actualmente el servicio de autenticación no está disponible. Intente mas tarde.'}}})

def logout(request: HttpRequest):
    url = 'http://127.0.0.1:4000/logout'
    # Hacemos la petición  para eliminar la cookie del token
    response = requests.get(url, cookies={'token': request.COOKIES.get('token')})
    # Eliminamos la cookie del token de la app
    django_response = redirect("/")
    django_response.delete_cookie('token')
    
    return django_response

