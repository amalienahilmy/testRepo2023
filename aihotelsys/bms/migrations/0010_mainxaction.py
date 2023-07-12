# Generated by Django 4.2.2 on 2023-06-30 16:27

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('bms', '0009_remove_expensesource_abbreviation'),
    ]

    operations = [
        migrations.CreateModel(
            name='MainXaction',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('is_deleted', models.BooleanField(default=False)),
                ('transaction_type', models.CharField(choices=[('income', 'Income'), ('expense', 'Expense')], max_length=10)),
                ('amount', models.DecimalField(decimal_places=2, max_digits=8)),
                ('remark', models.CharField(max_length=200)),
                ('date', models.DateField()),
                ('expense_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bms.expensesource')),
                ('hotel', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='bms.hotel')),
                ('income_source', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='bms.incomesource')),
                ('updated_by', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]