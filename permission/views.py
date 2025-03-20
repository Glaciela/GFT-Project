from django.shortcuts import render

# Create your views here.

def home(request):
    return render( request, 'permission/pages/home.html', context={'name':'Teste'})

def permissionview(request,id):
    return render(request, 'permission/pages/permissionview.html')

def teste(request):
    return render(request, 'global/home.html')