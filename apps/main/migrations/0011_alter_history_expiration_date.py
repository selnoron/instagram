# Generated by Django 4.2.7 on 2023-12-23 21:06

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0010_alter_history_expiration_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 21, 6, 9, 593279, tzinfo=datetime.timezone.utc)),
        ),
    ]
