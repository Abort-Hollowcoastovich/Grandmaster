# Generated by Django 4.0.6 on 2022-08-22 20:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0008_alter_document_image_alter_user_diploma_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='trainer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to=settings.AUTH_USER_MODEL),
        ),
    ]