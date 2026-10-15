from django.shortcuts import render
from .models import producto

def crear(request):
    if request.method == 'POST':
        Producto = producto(
            nombre = request.POST["nombre"],
            descripcion = request.POST["descripcion"],
            precio = request.POST["precio"],
            stock = request.POST["stock"],
            fecha = request.POST["fecha"]
        )
        Producto.save()
    return render(request, "formulario.html")

def listar(request):
    #Select * from productos
    productos = producto.objects.all()
    return render(
        request,
        "lista.html",
        {"productos": productos}
    )

#Consultar la información de un registro
def detalle(request,id):
    Producto = producto.objects.get(id=id) #SELECT * FROM productos WHERE id=7
    return render(
        request, 
        "detalle.html",
        {"Producto": Producto})

def editar(request, id):
    Producto = producto.objects.get(id=id)#SELECT * FROM productos WHERE id=7
    
    if request.method=="POST":#Si se van a guardar los cambios
        Producto.nombre = request.POST["nombre"] #Cambiar el nombre
        Producto.descripcion = request.POST["descripcion"] #Cambiar la descripción
        Producto.precio = request.POST["precio"] #Cambiar el precio
        Producto.stock = request.POST["stock"] #Cambiar el stock
        Producto.fecha = request.POST["fecha"] #Cambiar la fecha
        Producto.save() #Guardar los cambios

        return render(
            request,
            "detalle.html",
            {"Producto": Producto}
        )
    return render(
        request,
        "formulario.html",
        {"Producto": Producto}
    )

def eliminar(request,id):
    Producto = producto.objects.get(id=id)#SELECT * FROM productos WHERE id=7
    Producto.delete() #DELETE * FROM productos WHERE id= 7
    return render(
        request,
            "lista.html",
            {"Producto": Producto}
        )