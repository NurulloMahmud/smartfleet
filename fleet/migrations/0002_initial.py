# Generated by Django 4.2.9 on 2024-01-17 12:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('management', '0001_initial'),
        ('hiring', '0001_initial'),
        ('fleet', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='truckinuse',
            name='drivers',
            field=models.ManyToManyField(to='hiring.driver'),
        ),
        migrations.AddField(
            model_name='truckinuse',
            name='truck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.truck'),
        ),
        migrations.AddField(
            model_name='truck',
            name='carrier',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='management.company'),
        ),
        migrations.AddField(
            model_name='truck',
            name='make',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.truckmake'),
        ),
        migrations.AddField(
            model_name='truck',
            name='model',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='fleet.truckmodel'),
        ),
    ]
