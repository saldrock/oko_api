# Generated by Django 3.0.2 on 2020-03-06 13:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0009_auto_20200306_1221'),
    ]

    operations = [
        migrations.AddField(
            model_name='devices',
            name='room_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='house.Rooms'),
        ),
    ]