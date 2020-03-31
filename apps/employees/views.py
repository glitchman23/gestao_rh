from django.contrib.auth.models import User
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView, CreateView

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


class EmployeeCreate(CreateView):
    model = Employee
    fields = ['name', 'teams']

    def form_valid(self, form):
        employee = form.save(commit=False)
        username = employee.name.split(' ')[0]+employee.name.split(' ')[1]
        employee.company = self.request.user.employee.company
        employee.user = User.objects.create(username=username)
        employee.save()
        return super(EmployeeCreate, self).form_valid(form)