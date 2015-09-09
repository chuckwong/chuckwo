# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='blogspost',
            name='author',
            field=models.CharField(default='chuck', max_length=150),
            preserve_default=False,
        ),
    ]
