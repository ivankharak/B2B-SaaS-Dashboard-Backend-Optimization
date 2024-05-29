from django.shortcuts import render
from django.core.paginator import Paginator
from django.db.models import Q
from .models import AppUser

def user_list(request):
    search_query = request.GET.get('search', '')
    sort_by = request.GET.get('sort_by', 'id')
    page = request.GET.get('page', 1)
    page_size = request.GET.get('page_size', 10)

    # Joining all three tables: AppUser, Address, and CustomerRelationship
    users = AppUser.objects.select_related('address').prefetch_related('customerrelationship_set').all()

    if search_query:
        users = users.filter(
            Q(first_name__icontains=search_query) |
            Q(last_name__icontains=search_query) |
            Q(customer_id__icontains=search_query)
        )

    if sort_by:
        users = users.order_by(sort_by)

    paginator = Paginator(users, page_size)
    users_page = paginator.get_page(page)

    context = {
        'users': users_page,
        'search_query': search_query,
        'sort_by': sort_by,
        'page_size': page_size,
    }

    return render(request, 'user_list.html', context)
