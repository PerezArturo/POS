from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import Http404, HttpResponseRedirect
from django.urls import reverse

from .models import Categoria, SubCategoria, Marca, UnidadMedida, Producto
from .forms import (CategoriaForm, EditarCategoriaForm, SubCategoriaForm, EditarSubCategoriaForm,
                    MarcaForm, EditarMarcaForm)


class CategoriaView(LoginRequiredMixin, ListView):
    model = Categoria
    template_name = 'categoria/index.html'
    context_object_name = "obj"
    login_url = "login"


class SubCategoriaView(LoginRequiredMixin, ListView):
    model = SubCategoria
    template_name = 'subcategoria/index.html'
    context_object_name = "obj"
    login_url = "login"


class MarcaView(LoginRequiredMixin, ListView):
    model = Marca
    template_name = 'marca/index.html'
    context_object_name = "obj"
    login_url = "login"


class CrearCategoriaView(LoginRequiredMixin, CreateView):
    model = Categoria
    template_name = "categoria/crear.html"
    form_class = CategoriaForm
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        cat = form.save(commit=False)
        cat.save()

        success_url = reverse('inv:lista-cat')

        return HttpResponseRedirect(success_url)


class CrearSubCategoriaView(LoginRequiredMixin, CreateView):
    model = SubCategoria
    template_name = "subcategoria/crear-sub.html"
    form_class = SubCategoriaForm
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        cat = form.save(commit=False)
        cat.save()

        success_url = reverse('inv:lista-subcat')

        return HttpResponseRedirect(success_url)


class CrearMarcaView(LoginRequiredMixin, CreateView):
    model = Marca
    template_name = "marca/crear.html"
    form_class = MarcaForm
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        cat = form.save(commit=False)
        cat.save()

        success_url = reverse('inv:lista-marca')

        return HttpResponseRedirect(success_url)


class EditarCategoriaView(LoginRequiredMixin, UpdateView):
    model = Categoria
    template_name = "categoria/editar.html"
    form_class = EditarCategoriaForm
    pk_url_kwarg = "cat_pk"
    context_object_name = 'cat'
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        cat = form.save(commit=False)
        cat.save()

        success_url = reverse('inv:lista-cat')

        return HttpResponseRedirect(success_url)


class EditarSubCategoriaView(LoginRequiredMixin, UpdateView):
    model = SubCategoria
    template_name = "subcategoria/editar-sub.html"
    form_class = EditarSubCategoriaForm
    pk_url_kwarg = "cat_pk"
    context_object_name = 'cat'
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        cat = form.save(commit=False)
        cat.save()

        success_url = reverse('inv:lista-subcat')

        return HttpResponseRedirect(success_url)


class EditarMarcaView(LoginRequiredMixin, UpdateView):
    model = Marca
    template_name = "marca/editar.html"
    form_class = EditarCategoriaForm
    pk_url_kwarg = "marca_pk"
    context_object_name = 'marca'
    login_url = "login"

    def form_valid(self, form):
        form.instance.uc = self.request.user
        cat = form.save(commit=False)
        cat.save()

        success_url = reverse('inv:lista-marca')

        return HttpResponseRedirect(success_url)


class EliminarCategoriaView(LoginRequiredMixin, DeleteView):
    model = Categoria
    template_name = "categoria/eliminar.html"
    pk_url_kwarg = "cat_pk"
    context_object_name = "cat"
    login_url = "login"

    def get_success_url(self):
        return reverse('inv:lista-cat')


class EliminarSubCategoriaView(LoginRequiredMixin, DeleteView):
    model = SubCategoria
    template_name = "subcategoria/eliminar-sub.html"
    pk_url_kwarg = "cat_pk"
    context_object_name = "cat"
    login_url = "login"

    def get_success_url(self):
        return reverse('inv:lista-subcat')


class EliminarMarcaView(LoginRequiredMixin, DeleteView):
    model = Marca
    template_name = "marca/eliminar.html"
    pk_url_kwarg = "marca_pk"
    context_object_name = "cat"
    login_url = "login"

    def get_success_url(self):
        return reverse('inv:lista-marca')
