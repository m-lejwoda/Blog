# Generated by Django 2.2.10 on 2020-08-16 17:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0005_auto_20200816_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(default='', upload_to=''),
        ),
    ]
