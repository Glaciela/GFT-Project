import math
from django.core.paginator import Paginator


def make_pagination_range(
        page_range,
        qty_pages,
        current_page,
):
    middle_range = math.ceil(qty_pages / 2)
    start_range = current_page - middle_range
    stop_range = current_page + middle_range
    total_pages = len(page_range)

    start_range_offset = abs(start_range) if start_range < 0 else 0

    if start_range < 0:
        start_range = 0
        stop_range += start_range_offset

    if stop_range > total_pages:
        start_range = start_range - abs(total_pages - stop_range)
   
    pagination = page_range[start_range:stop_range]

    if total_pages == 3:
        pagination = [1, 2, 3]

    return{
        'pagination': pagination,
        'page_range': page_range,
        'qty_pages': qty_pages,
        'current_page': current_page,
        'total_pages': total_pages,
        'start_range': start_range,
        'stop_range': stop_range,
        'first_page_out_of_range': current_page > middle_range,
        'last_page_out_of_range': stop_range < total_pages,
        'ponts_before': total_pages-3,

    }

    return page_range[start_range:stop_range]

def make_pagination(request, queryset, per_page=9, qty_pages=4):
    try:
        current_page = int(request.GET.get('page', 1))
    except ValueError:
        current_page = 1  

    paginator = Paginator(queryset, per_page) 
    pag_obj = paginator.page(current_page) 

    pagination_range = make_pagination_range(
        paginator.page_range,
        qty_pages,
        current_page,
    )

    return pag_obj, pagination_range

