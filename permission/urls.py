from django.urls import path
from . import views

app_name = 'permission'

urlpatterns = [
    path('', views.home, name='home'),
    path('permissao/search/', views.search, name='search'),
    path('permissao/interdiction/<int:interdiction_id>/', views.interdiction, name='interdiction'),
    path('permissao/<int:id>/', views.permissionview, name='permission'),
]