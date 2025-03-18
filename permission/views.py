from django.shortcuts import render

# Create your views here.

def home(request):
    return render( request, 'permission/pages/home.html', context={'name':'Teste'})

def permissionview(request):
    return render(request, 'permission/pages/permissionview.html')