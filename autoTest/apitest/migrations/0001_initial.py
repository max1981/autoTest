# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2018-10-13 18:30
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApiStep',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiName', models.CharField(max_length=128, verbose_name='\u63a5\u53e3\u540d\u79f0')),
                ('apiUrl', models.CharField(max_length=128, verbose_name='\u63a5\u53e3\u5730\u5740')),
                ('apiParamValue', models.CharField(max_length=128, verbose_name='\u53c2\u6570\u548c\u503c')),
                ('apiMethod', models.CharField(choices=[('get', 'get'), ('post', 'post'), ('put', 'put'), ('delete', 'delete'), ('patch', 'patch')], default='get', max_length=256, null=True, verbose_name='\u8bf7\u6c42\u65b9\u6cd5')),
                ('apiResult', models.CharField(max_length=256, verbose_name='\u9884\u671f\u7ed3\u679c')),
                ('apiStatus', models.BooleanField(verbose_name='\u662f\u5426\u901a\u8fc7')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
            ],
        ),
        migrations.CreateModel(
            name='Apitest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apiTestName', models.CharField(max_length=64, verbose_name='\u6d41\u7a0b\u63a5\u53e3\u540d\u79f0')),
                ('apiTestDesc', models.CharField(max_length=128, null=True, verbose_name='\u6d41\u7a0b\u63a5\u53e3\u63cf\u8ff0')),
                ('apiTester', models.CharField(max_length=32, verbose_name='\u6d4b\u8bd5\u8d1f\u8d23\u4eba')),
                ('apiTestResult', models.BooleanField(verbose_name='\u6d4b\u8bd5\u7ed3\u679c')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name='\u521b\u5efa\u65f6\u95f4')),
                ('Product', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='product.Product')),
            ],
            options={
                'verbose_name': '\u6d41\u7a0b\u573a\u666f\u63a5\u53e3',
                'verbose_name_plural': '\u6d41\u7a0b\u573a\u666f\u63a5\u53e3',
            },
        ),
        migrations.AddField(
            model_name='apistep',
            name='ApiTest',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apitest.Apitest'),
        ),
    ]
