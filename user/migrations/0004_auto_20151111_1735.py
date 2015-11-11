# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0003_auto_20151108_1451'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': ('can_rent', 'Can rent a book')},
        ),
    ]
