# Generated by Django 4.2.5 on 2023-09-10 11:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbackend', '0005_alter_playareadb_playareaimageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playareadb',
            name='playAreaImageUrl',
            field=models.ImageField(upload_to=''),
        ),
    ]
