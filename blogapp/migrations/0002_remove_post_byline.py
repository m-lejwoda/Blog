# Generated by Django 2.2.10 on 2020-08-01 19:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='byline',
        ),
    ]
