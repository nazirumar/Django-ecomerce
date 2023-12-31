# Generated by Django 4.2.7 on 2023-11-14 21:52

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Error',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('traceback', models.TextField()),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('url', models.URLField(blank=True, null=True)),
                ('server_name', models.CharField(db_index=True, max_length=128)),
            ],
        ),
        migrations.CreateModel(
            name='ErrorBatch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_name', models.CharField(max_length=128)),
                ('message', models.TextField()),
                ('traceback', models.TextField()),
                ('is_resolved', models.BooleanField(default=False)),
                ('times_seen', models.PositiveIntegerField(default=1)),
                ('last_seen', models.DateTimeField(default=datetime.datetime.now)),
                ('first_seen', models.DateTimeField(default=datetime.datetime.now)),
                ('url', models.URLField(blank=True, null=True)),
                ('server_name', models.CharField(db_index=True, max_length=128)),
                ('checksum', models.CharField(db_index=True, max_length=32)),
            ],
            options={
                'unique_together': {('class_name', 'server_name', 'checksum')},
            },
        ),
    ]
