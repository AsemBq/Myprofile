# Generated by Django 5.0.6 on 2024-05-31 21:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeFa', '0003_technology_tools'),
    ]

    operations = [
        migrations.CreateModel(
            name='OtherSkills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tittle', models.CharField(max_length=30)),
            ],
        ),
    ]
