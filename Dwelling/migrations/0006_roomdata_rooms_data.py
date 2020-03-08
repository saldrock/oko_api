# Generated by Django 3.0.4 on 2020-03-08 13:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Dwelling', '0005_auto_20200308_1316'),
    ]

    operations = [
        migrations.AddField(
            model_name='roomdata',
            name='rooms_data',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_data', to='Dwelling.Room'),
        ),
    ]
