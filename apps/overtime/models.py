from django.db import models

from apps.employees.models import Employee


class Overtime(models.Model):
    reason = models.CharField(max_length=100, help_text='Employee overtime reason')
    employee = models.ForeignKey(Employee, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.reason

