# Generated by Django 4.1.3 on 2022-11-07 14:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='newnote',
            name='user',
        ),
    ]
