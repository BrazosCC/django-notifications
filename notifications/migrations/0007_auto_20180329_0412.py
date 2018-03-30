# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-03-29 08:12
from __future__ import unicode_literals

from django.db import migrations, models, connection
import uuid

def create_uuids(apps, schema_editor):

    Notification = apps.get_model('notifications', 'Notification')

    ids = [ x.get('id') for x in Notification.objects.all().values()]


    cursor = connection.cursor()

    for id in ids:
        cursor.execute("update notifications_notification set id = '{0}' where id = '{1}'".format(uuid.uuid4(), id))


class Migration(migrations.Migration):

    dependencies = [
        ('notifications', '0006_indexes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notification',
            name='id',
            field=models.CharField(max_length=50, primary_key=True, serialize=False),
        ),
        migrations.RunPython(create_uuids, reverse_code=migrations.RunPython.noop),

    ]
