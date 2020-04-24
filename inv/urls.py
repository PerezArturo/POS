from django.urls import path
from .views import CategoriaView
app_name = "inv"
urlpatterns = [
    path('', CategoriaView.as_view(), name="lista-cat"),
]
