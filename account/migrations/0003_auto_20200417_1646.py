# Generated by Django 3.0.4 on 2020-04-17 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_account_unsecure'),
    ]

    operations = [
        migrations.AddField(
            model_name='account_unsecure',
            name='password',
            field=models.CharField(default='Null', max_length=50),
        ),
        migrations.AddField(
            model_name='account_unsecure',
            name='password2',
            field=models.CharField(default='Null', max_length=50),
        ),
    ]