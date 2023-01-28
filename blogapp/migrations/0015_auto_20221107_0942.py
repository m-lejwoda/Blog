# Generated by Django 2.2 on 2022-11-07 09:42

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0014_auto_20221106_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='editorprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='editor', to=settings.AUTH_USER_MODEL),
        ),
    ]