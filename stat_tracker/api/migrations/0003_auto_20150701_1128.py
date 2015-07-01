# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_activity_user'),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='stat',
            unique_together=set([('timestamp', 'activity')]),
        ),
    ]
