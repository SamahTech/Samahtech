from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

app_name = 'app'

urlpatterns = [
    path('', views.home, name='home'),
    path('login', views.login, name='login'),
    path('units', views.units, name='units'),
]


urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
