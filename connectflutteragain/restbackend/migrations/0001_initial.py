# Generated by Django 4.2.5 on 2023-09-09 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PlayAreaDB',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('playAreaName', models.CharField(max_length=50)),
                ('playAreaSports', models.CharField(max_length=20)),
                ('playAreaLocation', models.CharField(max_length=100)),
            ],
        ),
    ]
