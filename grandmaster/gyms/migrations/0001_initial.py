# Generated by Django 4.0.6 on 2022-08-18 16:30

from django.db import migrations, models
import gyms.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Gym',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=256)),
                ('description', models.TextField(blank=True)),
                ('address', models.CharField(max_length=256)),
                ('cover', models.ImageField(upload_to=gyms.models.GymsPathAndHash('covers'))),
                ('order', models.PositiveIntegerField()),
            ],
            options={
                'db_table': 'gyms',
                'ordering': ['order'],
            },
        ),
    ]