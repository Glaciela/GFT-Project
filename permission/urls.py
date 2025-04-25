from django.urls import path
from . import views

app_name = 'permission'

urlpatterns = [
    path('', views.home, name='home'),
    path('permissao/interdiction/<int:interdiction_id>/', views.interdiction, name='interdiction'),
    path('permissao/<int:id>/', views.permissionview, name='permission'),
    path('permissao/search/', lambda request: ..., name='search'),
]