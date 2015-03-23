# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diaries', '0002_auto_20150315_0156'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='User_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachments',
            name='Achievement_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='Achievement_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='User_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='likes',
            name='Achievement_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='likes',
            name='User_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tags',
            name='Achievement_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tags',
            name='User_ID',
            field=models.IntegerField(default=0),
            preserve_default=True,
        ),
    ]
