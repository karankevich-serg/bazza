# Generated by Django 3.1.8 on 2021-04-15 09:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0023_auto_20210415_0951'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='object',
            name='streamDirection',
        ),
    ]