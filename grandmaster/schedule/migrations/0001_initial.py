# Generated by Django 4.0.6 on 2022-08-18 16:30

from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('sport_groups', '0002_sportgroup_trainer_alter_sportgroup_members'),
        ('gyms', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Schedule',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('weekday', models.CharField(choices=[('MN', 'Monday'), ('TU', 'Tuesday'), ('WE', 'Wednesday'), ('TH', 'Thursday'), ('FR', 'Friday'), ('SA', 'Saturday'), ('SU', 'Sunday')], max_length=10)),
                ('start_time', models.TimeField()),
                ('finish_time', models.TimeField()),
                ('group', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedules', to='sport_groups.sportgroup')),
                ('gym', models.ForeignKey(null=True, on_delete=django.db.models.deletion.DO_NOTHING, related_name='schedules', to='gyms.gym')),
            ],
            options={
                'db_table': 'schedule',
            },
        ),
        migrations.AddConstraint(
            model_name='schedule',
            constraint=models.CheckConstraint(check=models.Q(('finish_time__gte', django.db.models.expressions.F('start_time'))), name='finish_time_gte_start_time'),
        ),
    ]