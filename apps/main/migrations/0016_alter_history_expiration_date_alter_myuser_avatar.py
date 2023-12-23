# Generated by Django 4.2.7 on 2023-12-23 21:50

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0015_alter_history_expiration_date_alter_myuser_avatar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='expiration_date',
            field=models.DateTimeField(default=datetime.datetime(2023, 12, 24, 21, 50, 41, 844336, tzinfo=datetime.timezone.utc)),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='avatar',
            field=models.ImageField(default='avatars/unknown.png', upload_to='avatars/', verbose_name='изображение'),
        ),
    ]