# Generated by Django 4.0.6 on 2022-08-24 14:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('schedule', '0006_alter_schedule_weekday'),
        ('visit_log', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='visitlog',
            name='day',
        ),
        migrations.AddField(
            model_name='visitlog',
            name='attending',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='visitlog',
            name='mark_datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='visitlog',
            name='schedule',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='visit_logs', to='schedule.schedule'),
        ),
    ]