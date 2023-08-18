from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.urls import reverse_lazy
from .models import *
from django.contrib.auth import authenticate, login
from .forms import *
from django.contrib.auth.decorators import login_required
# Create your views here.

def Yo(request):
    return render(request, "aplicacion/YO.html")

@login_required
def home(request):
    return render(request, "aplicacion/home.html")
@login_required
def about(request):
    return render(request, "aplicacion/about.html")
@login_required
def aplicacion(request):
    return render(request, "aplicacion/aplicacion.html")
@login_required
def descuentos(request):
    return render(request, "aplicacion/descuentos.html")
@login_required
def populares(request):
    return render(request, "aplicacion/populares.html")
@login_required
def todos(request):
    ctx ={"todos":Todos.objects.all}
    return render (request,"aplicacion/todos.html", ctx)
@login_required
def carrito(request):
    ctx ={"carritos":Carrito.objects.all}
    return render (request,"aplicacion/carrito.html", ctx)
@login_required
def updateCarrito(request,id_curso):
    curso=Carrito.objects.get(id=id_curso)
    if request.method == "POST":
        miForm=CursosForm(request.POST)
        if miForm.is_valid():
            curso.nombre = miForm.cleaned_data.get('nombre')
            curso.precio = miForm.cleaned_data.get('precio')
            curso.precio_descuento = miForm.cleaned_data.get('precio_descuento')
            curso.save()
            return redirect(reverse_lazy('carrito'))   
    else:
        miForm = CursosForm(initial={'nombre':curso.nombre, 
                                    'precio':curso.precio, 
                                    'precio_descuento':curso.precio_descuento})         
    return render(request, "aplicacion/cursoForm.html", {'form': miForm})   
@login_required
def deleteCarrito(request,id_curso):
    curso=Carrito.objects.get(id=id_curso)
    curso.delete()
    return redirect(reverse_lazy('carrito'))  

@login_required
def createCarrito(request):
    if request.method == "POST":
        miForm = CursosForm(request.POST)
        if miForm.is_valid():
            p_nombre = miForm.cleaned_data.get('nombre')
            p_precio = miForm.cleaned_data.get('precio')
            p_precio_descuento = miForm.cleaned_data.get('precio_descuento')
            curso = Carrito(nombre=p_nombre, 
                             precio=p_precio,
                             precio_descuento=p_precio_descuento,)
            curso.save()
            return redirect(reverse_lazy('carrito'))
    else:
        miForm = CursosForm()

    return render(request, "aplicacion/CursosForm.html", {"form":miForm})

@login_required
def buscarCurso(request):
    return render(request,"aplicacion/buscarCurso.html")
@login_required
def buscar2(request):
    if request.GET['curso']:
        curso=request.GET['curso']
        cursos_encontrados = Todos.objects.filter(nombre__icontains=curso)
        return render(request, "aplicacion/resultadosCursos.html",{"cursos": curso})
    return HttpResponse("no se ingresaron datos")

def login_request(request):
    if request.method == "POST":
        miForm = AuthenticationForm(request, data=request.POST)
        if miForm.is_valid():
            usuario = miForm.cleaned_data.get('username')
            clave = miForm.cleaned_data.get('password')
            user = authenticate(username=usuario, password=clave)
            if user is not None:
                login(request, user)
                return render (request,"aplicacion/base.html", {"mensaje": f"bienvenido{usuario}"})
            else:
                return render (request,"aplicacion/login.html", {"form":miForm,"mensaje": f"datos invalidos"})
        else:
            return render (request,"aplicacion/login.html", {"form":miForm,"mensaje": f"datos invalidos"})
    
    miForm=AuthenticationForm()
    return render (request,"aplicacion/login.html",{"form":miForm})

def register(request):
    if request.method == 'POST':
        form = RegistroUsuariosForm(request.POST) # UserCreationForm 
        if form.is_valid():  # Si pasó la validación de Django
            usuario = form.cleaned_data.get('username')
            form.save()
            return render(request, "aplicacion/base.html", {"mensaje":"Usuario Creado"})        
    else:
        form = RegistroUsuariosForm() # UserCreationForm 

    return render(request, "aplicacion/registro.html", {"form": form})

@login_required
def editarPerfil(request):
    usuario = request.user
    if request.method == "POST":
        form = UserEditForm(request.POST)
        if form.is_valid():
            usuario.email = form.cleaned_data.get('email')
            usuario.password1 = form.cleaned_data.get('password1')
            usuario.password2 = form.cleaned_data.get('password2')
            usuario.first_name = form.cleaned_data.get('first_name')
            usuario.last_name = form.cleaned_data.get('last_name')
            usuario.save()
            return render(request, "aplicacion/base.html", {'mensaje': f"Usuario {usuario.username} actualizado correctamente"})
        else:
            return render(request, "aplicacion/editarPerfil.html", {'form': form})
    else:
        form = UserEditForm(instance=usuario)
    return render(request, "aplicacion/editarPerfil.html", {'form': form, 'usuario':usuario.username})

@login_required
def agregarAvatar(request):
    if request.method == "POST":
        form = AvatarFormulario(request.POST, request.FILES)
        if form.is_valid():
            u = User.objects.get(username=request.user)
            #borrar el avatar anterior
            avatarViejo = Avatar.objects.filter(user=u)
            if len(avatarViejo) > 0:
                avatarViejo[0].delete()

            #avatar nuevo
            avatar = Avatar(user=u, imagen=form.cleaned_data['imagen'])
            avatar.save()

            imagen = Avatar.objects.get(user=request.user.id).imagen.url
            request.session['avatar'] = imagen

            return render(request, "aplicacion/base.html")
    else:
        form = AvatarFormulario()
    return render(request, "aplicacion/agregarAvatar.html", {'form': form})