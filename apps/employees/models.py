from django.db import models

from django.contrib.auth.models import User

from apps.companies.models import Company
from apps.teams.models import Team


class Employee(models.Model):
    name = models.CharField(max_length=100, help_text='Employee name')
    user = models.OneToOneField(User, on_delete=models.PROTECT, null=True)
    teams = models.ManyToManyField(Team)
    company = models.ForeignKey(Company, on_delete=models.PROTECT, null=True)

    def __str__(self):
        return self.name
