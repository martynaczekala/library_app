# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('shelf', '0003_remove_bookitem_cover_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.AutoField(serialize=False, verbose_name='ID', primary_key=True, auto_created=True)),
                ('when', models.DateTimeField(default=django.utils.timezone.now)),
                ('returned', models.DateTimeField(blank=True, null=True)),
                ('what', models.ForeignKey(to='shelf.BookItem')),
                ('who', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
