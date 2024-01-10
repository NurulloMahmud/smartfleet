# Generated by Django 5.0.1 on 2024-01-10 12:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('fleet', '0003_alter_truck_driver'),
        ('hiring', '0002_driver_company_driver_middle_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='truck',
            name='driver',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='assigned_trucks', to='hiring.driver'),
        ),
    ]