from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView

from apps.employees.models import Employee


class EmployeeList(ListView):
    model = Employee

    def get_queryset(self):
        user_company = self.request.user.employee.company
        queryset = Employee.objects.filter(company=user_company)

        return queryset


class EmployeeUpdate(UpdateView):
    model = Employee
    fields = ['name', 'teams']


class EmployeeDelete(DeleteView):  
    model = Employee
    success_url = reverse_lazy('employee_list')
