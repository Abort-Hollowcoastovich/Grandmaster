# Generated by Django 4.0.6 on 2022-08-12 15:48

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport_groups', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='sportgroup',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='my_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sportgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='sport_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]
