"""
URL configuration for AprendiendoDjango project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
#Importar app con mis vistas
from miapp import views
#También se puede importar de la siguiente manera
# import miapp.views, pero para usarla se debe hacer de la siguiente manera:
#path('inicio/',miapp.views.index, name = 'inicio')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index, name="index"),
    path('inicio/',views.index, name="inicio"),
    path('hola-mundo/', views.hola_mundo, name ="hola_mundo"),
    path('pagina/',views.pagina, name = "pagina"),
    path('pagina/<int:redirigir>',views.pagina, name = "pagina"),
    # path('contacto/<str:nombre>/<str:apellidos>',views.contacto, name = "contacto" )
    path('contacto/',views.contacto, name="Contacto")
]
