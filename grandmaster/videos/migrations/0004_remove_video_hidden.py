# Generated by Django 4.0.6 on 2022-08-20 20:25

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('videos', '0003_video_hidden'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='video',
            name='hidden',
        ),
    ]
