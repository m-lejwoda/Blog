# Generated by Django 2.2 on 2022-11-05 11:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blogapp', '0010_auto_20221105_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='article',
            name='symbol',
        ),
        migrations.AddField(
            model_name='article',
            name='editor_profile',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='blogapp.EditorProfile'),
        ),
        migrations.AlterField(
            model_name='article',
            name='category',
            field=models.CharField(choices=[('News', 'News'), ('Filmy i Seriale', 'Filmy i Seriale'), ('Blog', 'Blog'), ('Hardkor', 'Hardkor')], default='News', max_length=20),
        ),
        migrations.DeleteModel(
            name='Category',
        ),
    ]