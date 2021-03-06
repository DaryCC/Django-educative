# Generated by Django 2.2.12 on 2022-03-23 22:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0003_accessrecord_prueba'),
    ]

    operations = [
        migrations.AlterField(
            model_name='topic',
            name='top_name',
            field=models.CharField(help_text='Escribe nombre del tema', max_length=264, unique=True),
        ),
        migrations.AlterField(
            model_name='webpage',
            name='topic',
            field=models.ForeignKey(help_text='Escribe el nombre de la página.', on_delete=django.db.models.deletion.CASCADE, to='firstapp.Topic'),
        ),
    ]
