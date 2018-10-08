# Generated by Django 2.1.2 on 2018-10-07 19:58

import datetime
from django.db import migrations, models
from django.utils.timezone import utc
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CompletedTask',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('created', models.DateTimeField(default=django.utils.timezone.now)),
                ('due_on', models.DateTimeField(default=datetime.datetime(2018, 10, 8, 19, 58, 50, 481499, tzinfo=utc))),
                ('owner', models.CharField(default='admin', max_length=100)),
                ('mark', models.BooleanField(default=True)),
            ],
        ),
        migrations.AlterField(
            model_name='task',
            name='due_on',
            field=models.DateTimeField(default=datetime.datetime(2018, 10, 8, 19, 58, 50, 473741, tzinfo=utc)),
        ),
        migrations.AlterField(
            model_name='task',
            name='owner',
            field=models.CharField(default='admin', max_length=100),
        ),
    ]
