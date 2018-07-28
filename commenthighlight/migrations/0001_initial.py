# Generated by Django 2.0.1 on 2018-07-28 14:49

import amo.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CommentHighlight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('modified', models.DateTimeField(auto_now=True)),
                ('video_id', models.CharField(max_length=255)),
                ('highlight_time', models.CharField(max_length=255)),
                ('is_active', models.BooleanField(default=True)),
            ],
            options={
                'db_table': 'CommentHighlight',
                'ordering': ('-created',),
            },
            bases=(amo.models.SearchMixin, amo.models.SaveUpdateMixin, models.Model),
        ),
    ]