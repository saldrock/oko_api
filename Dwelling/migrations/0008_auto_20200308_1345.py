# Generated by Django 3.0.4 on 2020-03-08 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Dwelling', '0007_auto_20200308_1329'),
    ]

    operations = [
        migrations.AddField(
            model_name='dwelling',
            name='dwelling_members',
            field=models.CharField(default='', max_length=50000),
        ),
        migrations.AddField(
            model_name='dwelling',
            name='dwelling_superUsers',
            field=models.CharField(default='', max_length=50000),
        ),
    ]
