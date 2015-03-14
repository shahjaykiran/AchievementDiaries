# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Achievements',
            fields=[
                ('Achievement_ID', models.AutoField(serialize=False, primary_key=True)),
                ('User_ID', models.IntegerField(default=0)),
                ('Achievement_Title', models.CharField(max_length=200)),
                ('Achievement_Description', models.TextField()),
                ('Achievement_Date', models.DateTimeField(verbose_name=b'Achievement Accomplished')),
                ('Achievement_Location', models.CharField(max_length=150)),
                ('Achievement_Attachments', models.TextField()),
                ('Achievement_Timestamp', models.DateTimeField(verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Attachments',
            fields=[
                ('Attachment_ID', models.AutoField(serialize=False, primary_key=True)),
                ('Achievement_ID', models.IntegerField(default=0)),
                ('Attachment_URL', models.CharField(max_length=200)),
                ('Attachment_Type', models.CharField(max_length=20)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Comments',
            fields=[
                ('Comment_ID', models.AutoField(serialize=False, primary_key=True)),
                ('User_ID', models.IntegerField(default=0)),
                ('Achievement_ID', models.IntegerField(default=0)),
                ('Comment', models.TextField()),
                ('Comment_Timestamp', models.DateTimeField(verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Likes',
            fields=[
                ('Like_ID', models.AutoField(serialize=False, primary_key=True)),
                ('User_ID', models.IntegerField(default=0)),
                ('Achievement_ID', models.IntegerField(default=0)),
                ('Like_Timestamp', models.DateTimeField(verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('Tag_ID', models.AutoField(serialize=False, primary_key=True)),
                ('User_ID', models.IntegerField(default=0)),
                ('Achievement_ID', models.IntegerField(default=0)),
                ('Tag', models.CharField(max_length=50)),
                ('Tag_Timestamp', models.DateTimeField(verbose_name=b'date created')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('User_ID', models.AutoField(serialize=False, primary_key=True)),
                ('User_Name', models.CharField(max_length=20)),
                ('User_Email', models.CharField(max_length=150)),
                ('User_Password', models.CharField(max_length=50)),
                ('User_Profile_Picture', models.CharField(max_length=50)),
                ('User_About', models.CharField(max_length=500)),
                ('User_Activation_Code', models.CharField(max_length=16)),
                ('User_Is_Activated', models.CharField(max_length=6)),
                ('User_Talent_Score', models.IntegerField(default=0)),
                ('User_Created_At', models.DateTimeField(verbose_name=b'date created')),
                ('User_Last_Login', models.DateTimeField(verbose_name=b'date last login')),
                ('User_Last_Logout', models.DateTimeField(verbose_name=b'date last logout')),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
