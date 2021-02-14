# Generated by Django 3.1.6 on 2021-02-13 09:42

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('realtors', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='realtor',
            name='is_pop',
            field=models.BooleanField(default=True),
        ),
        migrations.AlterField(
            model_name='realtor',
            name='is_mvp',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
    ]