# Generated by Django 2.1.3 on 2018-11-19 20:05

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('maquinas', '0003_auto_20181119_1605'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('setup', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Procedimento',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_inicio', models.DateTimeField(blank=True, null=True)),
                ('data_fim', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(max_length=20)),
                ('operador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Operador')),
            ],
        ),
        migrations.CreateModel(
            name='Processo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=100)),
                ('status', models.CharField(max_length=20)),
                ('gerente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Gerente')),
                ('maquina', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='maquinas.Maquinas')),
            ],
        ),
        migrations.AlterField(
            model_name='setup',
            name='status',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='procedimento',
            name='setup',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='setup.Setup'),
        ),
    ]
