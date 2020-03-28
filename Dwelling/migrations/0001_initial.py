# Generated by Django 3.0.4 on 2020-03-19 12:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Dwelling',
            fields=[
                ('dwelling_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('dwelling_name', models.CharField(default='', max_length=50)),
                ('dwelling_progress', models.IntegerField(default=0)),
                ('dwelling_code', models.CharField(default='', max_length=8)),
                ('dwelling_members', models.CharField(default='', max_length=50000)),
                ('dwelling_superUsers', models.CharField(default='', max_length=50000)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('room_id', models.IntegerField(default=0, primary_key=True, serialize=False)),
                ('room_name', models.CharField(default='', max_length=50)),
                ('dwelling_rooms', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='rooms', to='Dwelling.Dwelling')),
            ],
        ),
        migrations.CreateModel(
            name='Suggestion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('suggestion', models.CharField(default=0, max_length=150)),
                ('room_suggestion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='suggestion', to='Dwelling.Room')),
            ],
        ),
        migrations.CreateModel(
            name='RoomData',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('co2', models.CharField(default='', max_length=10485759)),
                ('humidity', models.CharField(default='', max_length=10485759)),
                ('tempurature', models.CharField(default='', max_length=10485759)),
                ('light', models.CharField(default='', max_length=10485759)),
                ('rooms_data', models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, related_name='room_data', to='Dwelling.Room')),
            ],
        ),
        migrations.CreateModel(
            name='Device',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('device_name', models.CharField(default='', max_length=50)),
                ('mac_adress', models.CharField(default='', max_length=50)),
                ('room_devices', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='devices', to='Dwelling.Room')),
            ],
        ),
    ]