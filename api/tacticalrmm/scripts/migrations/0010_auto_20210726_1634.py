# Generated by Django 3.2.1 on 2021-07-26 16:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('scripts', '0009_scriptsnippet'),
    ]

    operations = [
        migrations.AddField(
            model_name='scriptsnippet',
            name='desc',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='script',
            name='code_base64',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='script',
            name='description',
            field=models.TextField(blank=True, default='', null=True),
        ),
        migrations.AlterField(
            model_name='scriptsnippet',
            name='name',
            field=models.CharField(max_length=40, unique=True),
        ),
    ]