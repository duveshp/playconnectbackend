# Generated by Django 4.2.5 on 2023-09-10 10:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restbackend', '0004_alter_playareadb_playareaimageurl'),
    ]

    operations = [
        migrations.AlterField(
            model_name='playareadb',
            name='playAreaImageUrl',
            field=models.CharField(default='https://live-production.wcms.abc-cdn.net.au/28bc0d5bee1ab4b2b65dbb975ddb1b44?impolicy=wcms_crop_resize&cropH=788&cropW=1400&xPos=102&yPos=279&width=862&height=485', max_length=10000),
        ),
    ]
