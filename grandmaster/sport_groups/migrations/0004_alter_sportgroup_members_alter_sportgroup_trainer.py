# Generated by Django 4.0.6 on 2022-08-22 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('sport_groups', '0003_alter_sportgroup_members_alter_sportgroup_trainer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sportgroup',
            name='members',
            field=models.ManyToManyField(blank=True, related_name='sport_groups', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='sportgroup',
            name='trainer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='my_groups', to=settings.AUTH_USER_MODEL),
        ),
    ]