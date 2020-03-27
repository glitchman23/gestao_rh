from django.contrib import admin
from django.urls import path, include
from .views import EmployeeList, EmployeeUpdate, EmployeeDelete

urlpatterns = [
    path('', EmployeeList.as_view(), name='employee_list'),
    path('update/<int:pk>', EmployeeUpdate.as_view(), name='employee_update'),
    path('delete/<int:pk>', EmployeeDelete.as_view(), name='employee_delete'),
]
