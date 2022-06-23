from django.urls import path
from .views import index, contato, formulario

urlpatterns = [
    path('', index, name='index'),
    path('contato/', contato, name='contato'),
    path('formulario/', formulario, name='formulario'),
]