# Generated by Django 4.2.7 on 2023-12-23 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0009_alter_history_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 21, 6, 5, 684002, tzinfo=datetime.timezone.utc)),
        ),
    ]
