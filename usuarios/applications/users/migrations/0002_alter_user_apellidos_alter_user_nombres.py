# Generated by Django 4.1.3 on 2022-11-30 22:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='apellidos',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AlterField(
            model_name='user',
            name='nombres',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]
