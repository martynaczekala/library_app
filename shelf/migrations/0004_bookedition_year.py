# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shelf', '0003_remove_bookitem_cover_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='bookedition',
            name='year',
            field=models.CharField(default='', max_length=4),
        ),
    ]
