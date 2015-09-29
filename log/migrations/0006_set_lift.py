# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('log', '0005_remove_set_lift'),
    ]

    operations = [
        migrations.AddField(
            model_name='set',
            name='lift',
            field=models.ForeignKey(default=None, to='log.Lift'),
        ),
    ]
