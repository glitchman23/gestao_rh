from django.db import models
from django.urls import reverse


class Company(models.Model):
    name = models.CharField(max_length=100, help_text='Company name')

    class Meta:
        verbose_name_plural = "Companies"

    def get_absolute_url(self):
        return reverse('home')

    def __str__(self):
        return self.name
