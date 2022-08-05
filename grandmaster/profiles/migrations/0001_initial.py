# Generated by Django 4.0.6 on 2022-08-05 19:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import profiles.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='UserProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('b24_id', models.CharField(max_length=100, null=True)),
                ('first_name', models.CharField(max_length=100, null=True)),
                ('last_name', models.CharField(max_length=100, null=True)),
                ('middle_name', models.CharField(max_length=100, null=True)),
                ('birth_date', models.DateTimeField(null=True)),
                ('trainer', models.CharField(max_length=100, null=True)),
                ('city', models.CharField(max_length=200, null=True)),
                ('address', models.CharField(max_length=200, null=True)),
                ('school', models.CharField(max_length=200, null=True)),
                ('sport_school', models.CharField(max_length=200, null=True)),
                ('tech_qualification', models.CharField(max_length=100, null=True)),
                ('sport_qualification', models.CharField(max_length=100, null=True)),
                ('weight', models.IntegerField(null=True)),
                ('height', models.IntegerField(null=True)),
                ('med_certificate_date', models.DateTimeField(null=True)),
                ('insurance_policy_date', models.DateTimeField(null=True)),
                ('training_place', models.CharField(max_length=200, null=True)),
                ('phone_number', models.CharField(max_length=100, null=True)),
                ('region', models.CharField(max_length=200, null=True)),
                ('father_full_name', models.CharField(max_length=100, null=True)),
                ('father_birth_date', models.DateTimeField(null=True)),
                ('father_phone_number', models.CharField(max_length=100, null=True)),
                ('father_email', models.EmailField(max_length=254, null=True)),
                ('mother_full_name', models.CharField(max_length=100, null=True)),
                ('mother_birth_date', models.DateTimeField(null=True)),
                ('mother_phone_number', models.CharField(max_length=100, null=True)),
                ('mother_email', models.EmailField(max_length=254, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='profile', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'user_profiles',
            },
        ),
        migrations.CreateModel(
            name='Documents',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('passport_or_birth_certificate', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('passport_or_birth_certificate'))),
                ('oms_policy', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('oms_policy'))),
                ('school_ref', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('school_ref'))),
                ('insurance_policy', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('insurance_policy'))),
                ('tech_qual_diplo', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('tech_qual_diplo'))),
                ('med_certificate', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('med_certificate'))),
                ('foreign_passport', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('foreign_passport'))),
                ('inn', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('inn'))),
                ('diploma', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('diploma'))),
                ('snils', models.ImageField(null=True, upload_to=profiles.models.DocumentsPathAndHash('snils'))),
                ('user_profile', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='documents', to='profiles.userprofile')),
            ],
            options={
                'db_table': 'documents',
            },
        ),
    ]