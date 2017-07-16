# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-16 16:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wayfinder_app', '0009_auto_20170716_0738'),
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(blank=True, help_text='Enter the first name of user', max_length=100, null=True)),
                ('last_name', models.CharField(blank=True, help_text='Enter the last name', max_length=100, null=True)),
                ('occupation', models.CharField(blank=True, help_text='Enter the occupation name', max_length=100, null=True)),
                ('age', models.CharField(blank=True, help_text='Enter the age', max_length=100, null=True)),
                ('city', models.CharField(blank=True, help_text='Enter the city name', max_length=100, null=True)),
                ('state', models.CharField(blank=True, help_text='Enter the state name', max_length=100, null=True)),
                ('college', models.CharField(blank=True, help_text='Enter the college', max_length=100, null=True)),
                ('employer', models.CharField(blank=True, help_text='Enter the employer', max_length=100, null=True)),
                ('linkedin_link', models.CharField(blank=True, help_text='Enter the linkedin link', max_length=2083, null=True)),
                ('facebook_link', models.CharField(blank=True, help_text='Enter the facebook link', max_length=2083, null=True)),
                ('avatar_link', models.CharField(blank=True, help_text='Enter the avatar link', max_length=2083, null=True)),
            ],
        ),
    ]