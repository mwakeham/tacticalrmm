# Generated by Django 3.2.12 on 2022-04-01 23:01

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('checks', '0027_auto_20220401_2248'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='check',
            name='execution_time',
        ),
        migrations.RemoveField(
            model_name='check',
            name='extra_details',
        ),
        migrations.RemoveField(
            model_name='check',
            name='fail_count',
        ),
        migrations.RemoveField(
            model_name='check',
            name='history',
        ),
        migrations.RemoveField(
            model_name='check',
            name='last_run',
        ),
        migrations.RemoveField(
            model_name='check',
            name='more_info',
        ),
        migrations.RemoveField(
            model_name='check',
            name='outage_history',
        ),
        migrations.RemoveField(
            model_name='check',
            name='parent_check',
        ),
        migrations.RemoveField(
            model_name='check',
            name='retcode',
        ),
        migrations.RemoveField(
            model_name='check',
            name='status',
        ),
        migrations.RemoveField(
            model_name='check',
            name='stderr',
        ),
        migrations.RemoveField(
            model_name='check',
            name='stdout',
        ),
    ]