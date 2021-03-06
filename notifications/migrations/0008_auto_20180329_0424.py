# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 08:24
from __future__ import unicode_literals

from django.db import migrations, models, connection
import uuid

def migrate_field_to_uuid(apps, schema_editor):

    cursor = connection.cursor()
    cursor.execute('alter table notifications_notification alter column id drop default')
    cursor.execute('alter table notifications_notification alter column id type uuid using id::uuid')



class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0007_auto_20180329_0412'),
    ]

    operations = [
        migrations.RunPython(migrate_field_to_uuid, reverse_code=migrations.RunPython.noop),
    ]
