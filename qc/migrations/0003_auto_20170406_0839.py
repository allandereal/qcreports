# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-06 08:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('qc', '0002_auto_20170405_1639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='message',
            name='broadcast',
            field=models.IntegerField(null=True),
        ),
    ]