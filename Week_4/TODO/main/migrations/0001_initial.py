# Generated by Django 2.1.2 on 2018-10-06 17:26

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_on', models.DateTimeField(default=datetime.datetime(2018, 10, 7, 17, 26, 52, 412251, tzinfo=utc))),
                ('owner', models.CharField(max_length=100)),
                ('mark', models.BooleanField(default=False)),
            ],
        ),
    ]
