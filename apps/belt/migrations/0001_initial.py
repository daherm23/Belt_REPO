# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2018-01-26 19:05
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('login', '0004_auto_20180126_0925'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=350)),
                ('start_date', models.DateField()),
                ('end_date', models.DateField()),
                ('desc', models.CharField(max_length=350)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('companion', models.ManyToManyField(related_name='buddy_pass', to='login.User')),
                ('uploader', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trips', to='login.User')),
            ],
        ),
    ]
