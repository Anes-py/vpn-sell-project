from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns
from django.shortcuts import redirect

def redirect_to_fa(request):
    return redirect('/fa/')

urlpatterns = [
    path('', redirect_to_fa),
    path('admin/', admin.site.urls),
]

urlpatterns += i18n_patterns(
    path('', include('vpnshop.urls')),
)
