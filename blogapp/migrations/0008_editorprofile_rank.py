# Generated by Django 2.2.10 on 2020-08-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0007_editorprofile'),
    ]

    operations = [
        migrations.AddField(
            model_name='editorprofile',
            name='rank',
            field=models.CharField(default='Redaktor', max_length=100),
        ),
    ]
