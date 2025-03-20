from django.urls import path
from . import views



urlpatterns = [
    path('', views.home),
    path('permissao/<int:id>', views.permissionview),
    path('teste', views.teste),
]