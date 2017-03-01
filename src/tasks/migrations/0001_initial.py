# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-01 20:20
from __future__ import unicode_literals

from django.db import migrations, models


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
                ('description', models.TextField(blank=True, null=True)),
                ('status', models.CharField(choices=[('PEN', 'Pending'), ('DON', 'Done')], default='PEN', max_length=3)),
                ('time_estimated', models.IntegerField(null=True)),
                ('deadline', models.DateField(null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('modified_at', models.DateTimeField(auto_now=True)),
            ],
        ),
    ]
