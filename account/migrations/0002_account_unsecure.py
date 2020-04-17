# Generated by Django 3.0.4 on 2020-04-17 16:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Account_unsecure',
            fields=[
                ('email', models.EmailField(max_length=60, unique=True, verbose_name='email')),
                ('username', models.CharField(max_length=30, primary_key=True, serialize=False, unique=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_staff', models.BooleanField(default=False)),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('last_login', models.DateTimeField(auto_now=True, verbose_name='last_login')),
                ('is_active', models.BooleanField(default=True)),
                ('is_superuser', models.BooleanField(default=False)),
                ('dwelling_code', models.CharField(default='Null', max_length=50)),
                ('first_name', models.CharField(default='Null', max_length=50)),
                ('surname', models.CharField(default='Null', max_length=60)),
                ('incentivisation_choice', models.CharField(choices=[('SM', 'Save Money'), ('HE', 'Help Environment')], default='SM', max_length=16)),
                ('goal', models.IntegerField(null=True)),
                ('phone_number', models.CharField(default='', max_length=13)),
                ('admin_type', models.CharField(choices=[('SA', 'super_admin'), ('AD', 'admin'), ('NA', 'non_admin')], default='NA', max_length=2)),
                ('logged_in', models.BooleanField(default=True)),
            ],
        ),
    ]