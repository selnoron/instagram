# Generated by Django 4.2.7 on 2023-12-23 16:09

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_history_expiration_date_alter_likes_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 16, 9, 44, 286437, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='likes',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='likes', to=settings.AUTH_USER_MODEL, verbose_name='автор лайка'),
        ),
    ]
