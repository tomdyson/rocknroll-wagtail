# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-06-27 00:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_homepage_advert_url'),
    ]

    operations = [
        migrations.AlterField(
            model_name='homepage',
            name='site_description',
            field=models.TextField(blank=True, help_text='A brief explanation of this page.'),
        ),
    ]
