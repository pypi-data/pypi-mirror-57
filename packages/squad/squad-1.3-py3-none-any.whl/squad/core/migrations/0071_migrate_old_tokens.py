# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-02-05 17:25
from __future__ import unicode_literals

from django.db import migrations
from django.template.defaultfilters import slugify


def migrate_tokens(apps, schema_editor):
    OldToken = apps.get_model('core', 'Token')
    User = apps.get_model('auth', 'User')
    Token = apps.get_model('authtoken', 'Token')

    for old in OldToken.objects.all():
        username = slugify(old.description)
        user = User(username=username)
        user_group = None
        if old.project is None:
            # global token → "staff" user
            user.is_staff = True
        else:
            # project token → user member of the project group
            group = old.project.group
            user_group = group.user_groups.create(name='%s-submitters' % group.slug)
        i = 1
        while User.objects.filter(username=user.username).exists():
            user.username = '%s-%d' % (username, i)
            i += 1
        user.save()
        if user_group:
            user.groups.add(user_group)
        Token.objects.create(
            user=user,
            key=old.key[0:40],
        )


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0070_create_suite_test_and_metric_metadata'),
    ]

    operations = [
        migrations.RunPython(migrate_tokens)
    ]
