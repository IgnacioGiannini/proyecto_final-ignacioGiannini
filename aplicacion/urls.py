from django.urls import path, include
from .views import *
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', home, name="home" ),
    path('about/', about, name="about" ),
    path('descuentos/', descuentos, name="descuentos" ),
    path('populares/', populares, name="populares" ),
    path('todos/', todos, name="todos" ),
    path('aplicacion/', aplicacion, name="aplicacion" ),
    
    path('buscar_curso/', buscarCurso, name="buscar_curso" ),
    path('buscar2/', buscar2, name="buscar2" ),
    
    path('carrito/', carrito, name="carrito" ),
    path('updateCarrito/<int:id_curso>/', updateCarrito, name="updateCarrito" ),
    path('deleteCarrito/<int:id_curso>/', deleteCarrito, name="deleteCarrito" ),
    path('createCarrito/', createCarrito, name="createCarrito" ),
    
    path('login/', login_request, name="login" ),
    path('logout/', LogoutView.as_view(template_name="aplicacion/logout.html"), name="logout"),
    path('register/', register, name="register"),
    
    path('editar_perfil/', editarPerfil, name="editar_perfil"),
    path('agregar_avatar/', agregarAvatar, name="agregar_avatar"),
    path('Yo/', Yo, name="Yo"),
]