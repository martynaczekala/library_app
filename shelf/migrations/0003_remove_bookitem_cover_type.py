# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0002_auto_20151103_1836'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bookitem',
            name='cover_type',
        ),
    ]
