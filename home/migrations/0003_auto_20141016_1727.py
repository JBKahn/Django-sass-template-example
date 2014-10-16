# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_todo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='todo',
            old_name='status',
            new_name='is_done',
        ),
    ]
