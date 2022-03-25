# Generated by Django 2.2.12 on 2022-03-24 08:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('firstapp', '0006_auto_20220324_0549'),
    ]

    operations = [
        migrations.AddField(
            model_name='projects',
            name='team_lead',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='team_lead_reverse', to='firstapp.Employee'),
        ),
    ]
