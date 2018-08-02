# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('leads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Studentlogin',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=100)),
                ('eid', models.IntegerField()),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='dob',
            field=models.DateField(null=True, blank=True),
        ),
        migrations.AddField(
            model_name='student',
            name='email',
            field=models.EmailField(default=122, max_length=100),
            preserve_default=False,
        ),
    ]
