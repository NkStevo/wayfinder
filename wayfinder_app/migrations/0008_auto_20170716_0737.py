# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 14:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayfinder_app', '0007_auto_20170716_0727'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='avatar_link',
            field=models.CharField(blank=True, help_text='Enter the avatar link', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='facebook_link',
            field=models.CharField(blank=True, help_text='Enter the facebook link', max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='linkedin_link',
            field=models.CharField(blank=True, help_text='Enter the linkedin link', max_length=100, null=True),
        ),
    ]
