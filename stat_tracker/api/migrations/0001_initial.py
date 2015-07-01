# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Activity',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('title', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(verbose_name='ID', primary_key=True, serialize=False, auto_created=True)),
                ('timestamp', models.DateField(null=True)),
                ('stat', models.IntegerField()),
                ('activity', models.ForeignKey(to='api.Activity')),
            ],
        ),
    ]
