from django.urls import path
from .views import (CategoriaView, CrearCategoriaView, EditarCategoriaView, EliminarCategoriaView,
                    SubCategoriaView, CrearSubCategoriaView, EditarSubCategoriaView, EliminarSubCategoriaView,
                    MarcaView, CrearMarcaView, EditarMarcaView, marca_inactivar)
app_name = "inv"
urlpatterns = [
    path('categorias/', CategoriaView.as_view(), name="lista-cat"),
    path('categorias/crear/', CrearCategoriaView.as_view(), name="crear-cat"),
    path('categorias/editar/<int:cat_pk>/', EditarCategoriaView.as_view(), name="editar-cat"),
    path('categorias/eliminar/<int:cat_pk>/', EliminarCategoriaView.as_view(), name="eliminar-cat"),
    path('subcategorias/', SubCategoriaView.as_view(), name="lista-subcat"),
    path('subcategorias/crear/', CrearSubCategoriaView.as_view(), name="crear-subcat"),
    path('subcategorias/editar/<int:cat_pk>/', EditarSubCategoriaView.as_view(), name="editar-subcat"),
    path('subcategorias/eliminar/<int:cat_pk>/', EliminarSubCategoriaView.as_view(), name="eliminar-subcat"),
    path('marcas/', MarcaView.as_view(), name="lista-marca"),
    path('marcas/crear', CrearMarcaView.as_view(), name="crear-marca"),
    path('marcas/editar/<int:marca_pk>/', EditarMarcaView.as_view(), name="editar-marca"),
    path('marcas/inactivar/<int:id>/', marca_inactivar, name="eliminar-marca"),
]
