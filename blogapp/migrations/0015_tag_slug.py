# Generated by Django 2.2.10 on 2020-08-20 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_editorprofile_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='tag',
            name='slug',
            field=models.SlugField(blank=True, max_length=128, null=True),
        ),
    ]
