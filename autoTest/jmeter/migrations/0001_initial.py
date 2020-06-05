# -*- coding: utf-8 -*-
# Generated by Django 1.11.18 on 2019-01-17 08:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Jmeter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jxmName', models.CharField(max_length=32, verbose_name='\u811a\u672c\u540d\u79f0')),
                ('jxmPath', models.CharField(max_length=128, verbose_name='\u811a\u672c\u8def\u5f84')),
                ('description', models.CharField(max_length=256, verbose_name='\u63cf\u8ff0')),
                ('result', models.CharField(max_length=256, verbose_name='\u7ed3\u679c')),
            ],
            options={
                'verbose_name': '\u6027\u80fd\u6d4b\u8bd5\u811a\u672c',
                'verbose_name_plural': '\u6027\u80fd\u6d4b\u8bd5\u811a\u672c',
            },
        ),
    ]