# Generated by Django 4.2.5 on 2023-09-26 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbackend', '0009_userdb_playareadb_playareavendor'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendordb',
            name='VendorEmail',
            field=models.EmailField(default='playconnect@gmail.com', max_length=254),
        ),
        migrations.AddField(
            model_name='vendordb',
            name='VendorPassword',
            field=models.CharField(default='login123', max_length=30),
        ),
    ]