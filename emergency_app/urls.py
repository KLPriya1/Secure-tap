from django.contrib import admin
from django.urls import path, include
from alerts import views  # Import views from the alerts app
from django.views.generic import TemplateView  # Optional for home page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),  # Django auth URLs
    path('', views.home, name='home'),
    path('', include('alerts.urls')),  # Include alerts app URLs
    
]

    