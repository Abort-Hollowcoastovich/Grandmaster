# Generated by Django 4.0.6 on 2022-08-11 16:03

from django.db import migrations, models
import utils.image_path


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to=utils.image_path.PathAndHash('images'))),
            ],
            options={
                'db_table': 'images',
            },
        ),
    ]