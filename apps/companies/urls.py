from django.contrib import admin
from django.urls import path, include
from .views import CompanyCreate, CompanyUpdate

urlpatterns = [
    path('new', CompanyCreate.as_view(), name='company_create'),
    path('update/<int:pk>', CompanyUpdate.as_view(), name='company_update'),
]
