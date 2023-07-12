# Generated by Django 4.2.3 on 2023-07-10 13:14

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bms', '0018_alter_client_hotel_alter_client_updated_by_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='hotel',
        ),
        migrations.AddField(
            model_name='booking',
            name='amount_deposit',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='amount_due',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='amount_paid',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 21, 14, 41, 140712)),
        ),
        migrations.AddField(
            model_name='booking',
            name='isDeposit',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='booking',
            name='total_room_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 10, 21, 14, 41, 140712)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='client',
            name='hotel',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='bms.hotel'),
        ),
        migrations.AlterField(
            model_name='client',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
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
            name='hotel',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, on_delete=django.db.models.deletion.CASCADE, to='bms.hotel'),
        ),
        migrations.AlterField(
            model_name='mainxaction',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.CreateModel(
            name='RoomType',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('name', models.CharField(max_length=50)),
                ('type', models.CharField(max_length=30)),
                ('updated_by', models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('room_number', models.CharField(max_length=3)),
                ('base_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('isWindow', models.BooleanField(default=False)),
                ('remark', models.CharField(max_length=100)),
                ('room_type', models.ForeignKey(default='0000', on_delete=django.db.models.deletion.DO_NOTHING, to='bms.roomtype')),
                ('updated_by', models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='booking',
            name='Room',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.DO_NOTHING, to='bms.room'),
            preserve_default=False,
        ),
    ]
