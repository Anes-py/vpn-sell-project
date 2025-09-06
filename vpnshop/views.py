from django.shortcuts import render

from .models import Product, ServersLocations

def home_page_view(request):
    context = {
    'products':Product.objects.filter(is_active=True),
    'servers':ServersLocations.objects.filter(is_active=True),
    }
    return render(
        request,
        'vpnshop/home.html',
        context=context,
    )
