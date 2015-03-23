# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Diaries', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='achievements',
            name='User_ID',
            field=models.ForeignKey(to='Diaries.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='attachments',
            name='Achievement_ID',
            field=models.ForeignKey(to='Diaries.Achievements'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='Achievement_ID',
            field=models.ForeignKey(to='Diaries.Achievements'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='comments',
            name='User_ID',
            field=models.ForeignKey(to='Diaries.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='likes',
            name='Achievement_ID',
            field=models.ForeignKey(to='Diaries.Achievements'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='likes',
            name='User_ID',
            field=models.ForeignKey(to='Diaries.User'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tags',
            name='Achievement_ID',
            field=models.ForeignKey(to='Diaries.Achievements'),
            preserve_default=True,
        ),
        migrations.AlterField(
            model_name='tags',
            name='User_ID',
            field=models.ForeignKey(to='Diaries.User'),
            preserve_default=True,
        ),
    ]
