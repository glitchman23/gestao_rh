# Generated by Django 3.0.4 on 2020-03-31 12:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('documents', '0003_auto_20200326_1954'),
    ]

    operations = [
        migrations.AddField(
            model_name='document',
            name='file',
            field=models.FileField(default='', upload_to='documents'),
            preserve_default=False,
        ),
    ]
