# Generated by Django 4.2.7 on 2023-12-23 16:23

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_alter_history_expiration_date_alter_likes_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 16, 23, 34, 554684, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterUniqueTogether(
            name='likes',
            unique_together={('author', 'publication')},
        ),
    ]
