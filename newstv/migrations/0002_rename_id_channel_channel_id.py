# Generated by Django 4.2 on 2023-04-22 09:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newstv', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='channel',
            old_name='id',
            new_name='channel_id',
        ),
    ]