# Generated by Django 5.0.1 on 2024-01-15 11:09

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('fleet', '0006_truckstatus_truckinuse'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Case',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateField(auto_now_add=True)),
                ('shop_address', models.TextField(blank=True, null=True)),
                ('shop_name', models.CharField(blank=True, max_length=500, null=True)),
                ('shop_number', models.CharField(blank=True, max_length=50, null=True)),
                ('shop_in', models.DateTimeField(blank=True, null=True)),
                ('shop_out', models.DateTimeField(blank=True, null=True)),
                ('days_in_shop', models.IntegerField(blank=True, null=True)),
                ('amount', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('expense', models.CharField(max_length=500)),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.truck')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.status')),
            ],
        ),
        migrations.CreateModel(
            name='Note',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('note', models.TextField(blank=True, null=True)),
                ('case', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='maintenance.case')),
                ('staff', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Odometer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ododmeter', models.FloatField()),
                ('date', models.DateField(auto_now=True)),
                ('truck', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.truck')),
            ],
        ),
    ]