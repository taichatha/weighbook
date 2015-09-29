# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0002_set'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='lift',
            name='log',
        ),
        migrations.RemoveField(
            model_name='log',
            name='user',
        ),
        migrations.RemoveField(
            model_name='set',
            name='log',
        ),
        migrations.DeleteModel(
            name='Lift',
        ),
        migrations.DeleteModel(
            name='Log',
        ),
        migrations.DeleteModel(
            name='Set',
        ),
    ]
