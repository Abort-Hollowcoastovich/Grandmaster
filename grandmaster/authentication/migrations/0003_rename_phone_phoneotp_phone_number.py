# Generated by Django 4.0.6 on 2022-08-08 17:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0002_alter_user_parents'),
    ]

    operations = [
        migrations.RenameField(
            model_name='phoneotp',
            old_name='phone',
            new_name='phone_number',
        ),
    ]