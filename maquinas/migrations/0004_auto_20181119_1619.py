# Generated by Django 2.1.3 on 2018-11-19 20:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maquinas', '0003_auto_20181119_1605'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maquinas',
            name='status',
            field=models.CharField(blank=True, max_length=30, null=True),
        ),
        migrations.AlterField(
            model_name='maquinas',
            name='tipo',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maquinas.Tipo'),
        ),
    ]
