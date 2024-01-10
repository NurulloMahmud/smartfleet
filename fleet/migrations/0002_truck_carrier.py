# Generated by Django 4.2.9 on 2024-01-09 19:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0001_initial'),
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truck',
            name='carrier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.company'),
        ),
    ]