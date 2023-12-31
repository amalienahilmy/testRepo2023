# Generated by Django 4.2.3 on 2023-07-11 05:23

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.query


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bms', '0029_alter_booking_checkin_date_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booking',
            name='checkin_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 11, 13, 23, 27, 974306)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='checkout_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 7, 12, 14, 0)),
        ),
        migrations.AlterField(
            model_name='booking',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bookingplatform',
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
        migrations.AlterField(
            model_name='paymentmethod',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='room',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='roomtype',
            name='updated_by',
            field=models.ForeignKey(default=django.db.models.query.QuerySet.first, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL),
        ),
    ]
