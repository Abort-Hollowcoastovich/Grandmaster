# Generated by Django 4.0.6 on 2022-08-19 11:16

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import invoice.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Bill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service', models.CharField(choices=[('yookassa', 'Yookassa')], default='yookassa', max_length=256)),
                ('purpose', models.CharField(max_length=256)),
                ('amount', models.IntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('activated_at', models.DateTimeField()),
                ('_must_be_paid_at', models.DateTimeField()),
                ('is_periodic', models.BooleanField()),
                ('period', models.DurationField(null=True, validators=[invoice.models.validate_min])),
            ],
        ),
        migrations.CreateModel(
            name='PayAccount',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('account_id', models.CharField(max_length=256)),
                ('secret_key', models.CharField(max_length=256)),
                ('active', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yookassa_id', models.CharField(max_length=256, null=True)),
                ('active', models.BooleanField(default=True)),
                ('_paid', models.BooleanField(default=False)),
                ('paid_at', models.DateTimeField(null=True)),
                ('user_bill_number', models.IntegerField(null=True)),
                ('pay_account_bill_number', models.IntegerField(null=True)),
                ('bill', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bill_users', to='invoice.bill')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, related_name='bills', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.AddField(
            model_name='bill',
            name='pay_account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='invoice.payaccount'),
        ),
    ]