from django.shortcuts import render

# Create your views here.

from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
 
from .models import Alumno

from django.urls import reverse
from django.contrib import messages
from django.contrib.messages.views import SuccessMessageMixin
from django import forms




#----- ALTAS ------------
class CrearAlumno(SuccessMessageMixin, CreateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno AGREGADO correctamente!!!"
    def get_success_url(self):
        return reverse('listar')
#----- BAJAS ------------
class EliminarAlumno(SuccessMessageMixin, DeleteView):
    model = Alumno
    form = Alumno
    fields = "_"

    def get_success_url(self):
        succes_message = 'alumno ELIMINADO correctamente!!'
        messages.success(self.request, succes_message)
        return reverse('listar')
    

#----- CAMBIOS ------------
class ActualizarAlumno(SuccessMessageMixin, UpdateView):
    model = Alumno
    form = Alumno
    fields = "__all__"
    success_message = "Alumno ACTUALIZADO correctamente!!"

    def get_success_url(self):
        return reverse('listar')

#---- CONSULTAR UN ALUMNO
class DetalleAlumno(DetailView):
    model = Alumno

#----- CONSULTAR TODOS ALUMNOS
class ListarAlumnos(ListView):
    model = Alumno

from django.contrib.auth.views import LoginView

class CustomLoginView(LoginView):
    template_name = "alumnos/login.html"

