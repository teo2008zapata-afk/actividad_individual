from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User

#inicio de sesión
def iniciar_sesion(request):

    if request.method == 'POST':
        usuario =authenticate(request,
            username = request.POST['username'],
            password = request.POST['password']
        )
      
        if usuario is not None:
            login(request, usuario)
            destino = request.GET.get("next", "/productos/lista") # Redirigir a la página de inicio después del login
            return redirect(destino)

        return render(
        request,
        "usuarios/login.html",
        {"error": "Usuario o contraseña incorrectos."}
        )

    #redicreccionar si el metodo no es post
    return render(
        request,
        "usuarios/login.html",
    )

def cerrar_sesion(request):
    logout(request)
    return redirect("/usuarios/login/")

        