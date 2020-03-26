from django.db import models


class Document(models.Model):
    description = models.CharField(max_length=100, help_text='Document description')

    def __str__(self):
        return self.description
