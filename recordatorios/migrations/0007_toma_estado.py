# Generated by Django 5.1.6 on 2025-03-24 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recordatorios', '0006_relacioncuidadorpaciente'),
    ]

    operations = [
        migrations.AddField(
            model_name='toma',
            name='estado',
            field=models.CharField(choices=[('pendiente', 'Pendiente'), ('tomada', 'Tomada'), ('omitida', 'Omitida')], default='pendiente', max_length=10),
        ),
    ]
