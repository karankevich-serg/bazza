# Generated by Django 3.1.8 on 2021-04-13 08:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0010_auto_20210413_0834'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='leftside',
            name='BsTsmOut',
        ),
    ]
