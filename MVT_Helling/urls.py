from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static

from MVT_Helling.settings import MEDIA_ROOT, MEDIA_URL
from MVT_Helling.views import inicio, index


urlpatterns = [
    path('',index, name = 'index'),
    path('admin/', admin.site.urls),
    path('Inicio/',inicio),   
    
    
    path('fleet/', include ('fleet.url')),
    path('flights/', include('flights.url')),
    path('routes/', include('routes.url')),
    path('users/', include('users.url')),
    
    
] + static(MEDIA_URL, document_root = MEDIA_ROOT)
