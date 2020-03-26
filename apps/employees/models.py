from django.db import models


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text='Employee name')

    def __str__(self):
        return self.name
