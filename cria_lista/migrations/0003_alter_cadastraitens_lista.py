# Generated by Django 4.2.4 on 2023-09-03 23:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cria_lista', '0002_cadastraitens'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastraitens',
            name='lista',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='nome_lista', to='cria_lista.crialista'),
        ),
    ]
