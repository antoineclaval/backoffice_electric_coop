# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('coopInfo', '0003_auto_20150128_1526'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cooperative',
            old_name='address',
            new_name='mailAddress',
        ),
        migrations.AddField(
            model_name='cooperative',
            name='countiesServed',
            field=models.CharField(default='', max_length=500),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cooperative',
            name='streetAddress',
            field=models.CharField(default='', max_length=50),
            preserve_default=False,
        ),
    ]
