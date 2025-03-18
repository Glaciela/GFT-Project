from django.urls import path
from permission.views import permissionview, home



urlpatterns = [
    path('', home),
    path('permissao/', permissionview)
]