# Generated by Django 3.0.4 on 2020-03-31 14:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_remove_account_house_code'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='account',
            name='goal',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_house_admin',
        ),
        migrations.RemoveField(
            model_name='account',
            name='is_house_super',
        ),
        migrations.RemoveField(
            model_name='account',
            name='phone_number',
        ),
    ]