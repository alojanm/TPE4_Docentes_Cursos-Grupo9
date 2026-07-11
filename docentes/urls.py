from django.urls import path
from .views import ListaDocentes

urlpatterns = [
    path(
        "verDocentes/",
        ListaDocentes.as_view(),
        name="verDocentes"
    ),
]