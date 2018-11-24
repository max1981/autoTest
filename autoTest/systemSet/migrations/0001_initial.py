# -*- coding: utf-8 -*-
# Generated by Django 1.11.12 on 2018-10-20 09:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SystemSet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('urlName', models.CharField(max_length=32, verbose_name='\u73af\u5883\u540d\u79f0')),
                ('systemUrl', models.CharField(max_length=128, verbose_name='url')),
            ],
            options={
                'verbose_name': '\u7cfb\u7edf\u8bbe\u7f6e',
                'verbose_name_plural': '\u7cfb\u7edf\u8bbe\u7f6e',
            },
        ),
    ]
