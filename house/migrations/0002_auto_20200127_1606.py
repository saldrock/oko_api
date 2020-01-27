# Generated by Django 3.0.2 on 2020-01-27 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('house', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Devices',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=36)),
            ],
        ),
        migrations.AddField(
            model_name='room',
            name='AddDevice',
            field=models.BooleanField(default=False),
        ),
    ]