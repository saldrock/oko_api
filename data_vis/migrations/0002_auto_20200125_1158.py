# Generated by Django 3.0.2 on 2020-01-25 11:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_vis', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='period',
        ),
        migrations.CreateModel(
            name='DataType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Hum', 'Humidity'), ('Tem', 'Tempurature'), ('Co2', 'Co2 Level')], max_length=3)),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_vis.Room')),
            ],
            options={
                'unique_together': {('room', 'type')},
                'index_together': {('room', 'type')},
            },
        ),
        migrations.CreateModel(
            name='TimePeriod',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.CharField(choices=[('1hr', 'The Last Hour'), ('1d', '1 day Ago'), ('3d', '3 days Ago '), ('1w', '1 week ago')], max_length=3)),
                ('data', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_vis.DataType')),
                ('room', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_vis.Room')),
            ],
            options={
                'unique_together': {('room', 'data')},
                'index_together': {('room', 'data')},
            },
        ),
    ]