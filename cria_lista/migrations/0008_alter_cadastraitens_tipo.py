# Generated by Django 4.2.4 on 2023-09-10 14:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('cria_lista', '0007_cadastraitens_tipo'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cadastraitens',
            name='tipo',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='tipos_de_itens', to='cria_lista.tiposdeitens'),
        ),
    ]
