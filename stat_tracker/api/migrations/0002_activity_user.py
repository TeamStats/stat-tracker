# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.ForeignKey(null=True, to='users.Profile'),
        ),
    ]
