from django.shortcuts import render
from .models import pedido

def crear(request):
    if request.method == 'POST':
        Pedido = pedido(
            numero_pedido = request.POST["numero_pedido"],
            nombre_cliente = request.POST["nombre_cliente"],
            fecha = request.POST["fecha"],
            descripcion = request.POST["descripcion"],
            total = request.POST["total"],
            estado = request.POST["estado"],
            usuario = request.POST["usuario"]
        )
        Pedido.save()
    return render(request, "formulario1.html")

def listar(request):
    #Select * from pedidos
    pedidos = pedido.objects.all()
    return render(
        request,
        "lista1.html",
        {"pedidos":pedidos}
    )

#Consultar la información de un registro
def detalle(request,id):
    Pedido = pedido.objects.get(id=id) #SELECT * FROM pedidos WHERE id=7
    return render(
        request, 
        "detalle1.html",
        {"Pedido": Pedido})

def editar(request, id):
    Pedido = pedido.objects.get(id=id)#SELECT * FROM pedidos WHERE id=7
    
    if request.method=="POST":#Si se van a guardar los cambios
        Pedido.numero_pedido = request.POST["numero_pedido"] #Cambiar el número de pedido
        Pedido.nombre_cliente = request.POST["nombre_cliente"] #Cambiar el nombre del cliente
        Pedido.fecha = request.POST["fecha"] #Cambiar la fecha
        Pedido.descripcion = request.POST["descripcion"] #Cambiar la descripción
        Pedido.total = request.POST["total"] #Cambiar el total
        Pedido.estado = request.POST["estado"] #Cambiar el estado
        Pedido.usuario = request.POST["usuario"] #Cambiar el usuario

        Pedido.save() #Guardar los cambios

        return render(
            request,
            "detalle1.html",
            {"Pedido": Pedido}
        )
    return render(
        request,
        "formulario1.html",
        {"Pedido": Pedido}
    )

def eliminar(request,id):
    Pedido = pedido.objects.get(id=id)#SELECT * FROM pedidos WHERE id=7
    Pedido.delete() #DELETE * FROM pedidos WHERE id= 7
    return render(
            request,
            "lista1.html",
            {"Pedido":Pedido}
        )