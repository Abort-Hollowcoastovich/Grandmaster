# Generated by Django 4.0.6 on 2022-08-20 20:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('instructions', '0002_alter_instruction_link'),
    ]

    operations = [
        migrations.AddField(
            model_name='instruction',
            name='hidden',
            field=models.BooleanField(default=False),
        ),
    ]