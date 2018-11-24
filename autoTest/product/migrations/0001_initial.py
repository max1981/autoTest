# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-10 18:04
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(max_length=64, verbose_name='\u4ea7\u54c1\u540d\u79f0')),
                ('productdesc', models.CharField(max_length=200, verbose_name='\u4ea7\u54c1\u63cf\u8ff0')),
                ('producter', models.CharField(max_length=200, verbose_name='\u4ea7\u54c1\u8d1f\u8d23\u4eba')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
            options={
                'verbose_name': '\u4ea7\u54c1\u7ba1\u7406',
                'verbose_name_plural': '\u4ea7\u54c1\u7ba1\u7406',
            },
        ),
    ]
