# -*- coding: utf-8 -*-
# Generated by Django 1.11.14 on 2018-07-26 17:27
from __future__ import unicode_literals

from django.db import migrations


def update(apps, schema_editor):
    ProjectStatus = apps.get_model('core', 'ProjectStatus')
    for status in ProjectStatus.objects.all():
        build = status.build
        status.test_runs_total = build.test_runs.count()
        status.test_runs_completed = build.test_runs.filter(completed=True).count()
        status.test_runs_incomplete = build.test_runs.filter(completed=False).count()
        status.save()


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_cache_test_run_counts'),
    ]

    operations = [
        migrations.RunPython(update, reverse_code=migrations.RunPython.noop)
    ]
