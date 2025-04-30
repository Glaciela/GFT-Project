from django.shortcuts import render, get_list_or_404, get_object_or_404
from django.http import Http404
#from utils.permission.factory import make_permission
from .models import Permission

def home(request):
    permissions = Permission.objects.filter(
            authorized=True
        ).order_by('date_start')
      
    return render( request, 'permission/pages/home.html', context={
        'permissions':permissions,
        })

def interdiction(request, interdiction_id):
    permissions = get_list_or_404(
        Permission.objects.filter(
            reason__id=interdiction_id,
            authorized=True
        ).order_by('date_start')
        )
    
    return render( request, 'permission/pages/interdiction.html', context={
        'permissions':permissions,  
        'title': f'{permissions[0].reason.name} - Interdição | ',
        })

def permissionview(request,id):
    permission = get_object_or_404(Permission, pk=id, authorized=True)
       
    return render(request, 'permission/pages/permissionview.html', context={
    'permission':permission,
    'is_detail_page': True,
    })

def search(request):
    search_term = request.GET.get('q','').strip()
    if not search_term:
        raise Http404('Termo de busca não encontrado.')
    
    permissions = Permission.objects.filter(
        authorized=True,
        location__icontains=search_term,
    ).order_by('date_start')

    return render(request, 'permission/pages/search.html',
                  {
                      'page_title': f'Busca por "{search_term}" | ',
                      'search_term': search_term,
                      'permissions':permissions,
                  }
                  )