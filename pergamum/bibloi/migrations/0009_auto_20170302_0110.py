# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-03-02 07:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bibloi', '0008_article_uid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='article',
            name='source_file',
            field=models.FileField(max_length=1024, null=True, upload_to=''),
        ),
    ]