# -*- coding: utf-8 -*-
# Generated by Django 1.9.8 on 2017-04-10 09:38
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_auto_20170410_0727'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userhistory',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='histories', to=settings.AUTH_USER_MODEL),
        ),
    ]
