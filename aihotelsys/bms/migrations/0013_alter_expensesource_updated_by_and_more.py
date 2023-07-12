# Generated by Django 4.2.2 on 2023-07-07 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query
import django_countries.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bms', '0012_alter_mainxaction_remark'),
    ]

    operations = [
        migrations.AlterField(
            model_name='expensesource',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='hotel',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='incomesource',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='mainxaction',
            name='date',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='mainxaction',
            name='hotel',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='bms.hotel'),
        ),
        migrations.AlterField(
            model_name='mainxaction',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='Client',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('fullname', models.CharField(max_length=100)),
                ('nationality', django_countries.fields.CountryField(max_length=2)),
                ('passportNo', models.CharField(max_length=25)),
                ('mobileNo', models.CharField(max_length=25)),
                ('isRegular', models.BooleanField(default=False)),
                ('isBlacklisted', models.BooleanField(default=False)),
                ('hotel', models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='bms.hotel')),
                ('updated_by', models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
