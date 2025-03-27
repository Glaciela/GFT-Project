from django.shortcuts import render, get_list_or_404, get_object_or_404
from utils.permission.factory import make_permission
from .models import Permission

# Create your views here.

def home(request):
    permissions = get_list_or_404(
        Permission.objects.filter(
            is_publihed=True
        ).order_by('date_start')
        )
      
    return render( request, 'permission/pages/home.html', context={
        'permissions':permissions,  
        })

def interdiction(request, interdiction_id):
    permissions = get_list_or_404(
        Permission.objects.filter(
            reason__id=interdiction_id,
            is_publihed=True
        ).order_by('date_start')
        )
    
    return render( request, 'permission/pages/interdiction.html', context={
        'permissions':permissions,  
        'title': f'{permissions[0].reason.name} - Interdição | ',
        })

def permissionview(request,id):
    permission = get_object_or_404(Permission, pk=id, is_publihed=True)
       
    return render(request, 'permission/pages/permissionview.html', context={
    'permission':permission,
    'is_detail_page': True,
    })