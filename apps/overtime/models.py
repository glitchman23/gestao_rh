from django.db import models


class Overtime(models.Model):
    reason = models.CharField(max_length=100, help_text='Employee overtime reason')

    def __str__(self):
        return self.reason

