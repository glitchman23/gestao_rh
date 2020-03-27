from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('apps.homepage.urls')),
    path('employees/', include('apps.employees.urls')),
    path('companies/', include('apps.companies.urls')),
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),
]
