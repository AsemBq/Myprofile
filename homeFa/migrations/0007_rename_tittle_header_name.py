# Generated by Django 5.0.6 on 2024-05-31 22:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('homeFa', '0006_project_code_project_tech'),
    ]

    operations = [
        migrations.RenameField(
            model_name='header',
            old_name='tittle',
            new_name='name',
        ),
    ]
