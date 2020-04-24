from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView
from .models import Categoria


class CategoriaView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'index.html'
    context_object_name = "obj"
    login_url = "login"
