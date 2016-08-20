# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, serialize=False, primary_key=True, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('tag', models.CharField(blank=True, max_length=20, null=True)),
                ('image', models.ImageField(blank=True, upload_to='image', null=True)),
                ('views', models.IntegerField(default=0)),
                ('slug', models.CharField(unique=True, max_length=100)),
            ],
        ),
    ]
