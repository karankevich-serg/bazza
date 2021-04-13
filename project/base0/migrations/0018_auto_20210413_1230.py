# Generated by Django 3.1.8 on 2021-04-13 12:30

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0017_auto_20210413_1226'),
    ]

    operations = [
        migrations.RenameField(
            model_name='matrix',
            old_name='BsTsmIn',
            new_name='bsTsmIn',
        ),
        migrations.RenameField(
            model_name='matrix',
            old_name='BsTsmOut',
            new_name='bsTsmOut',
        ),
        migrations.RemoveField(
            model_name='leftside',
            name='hw',
        ),
        migrations.AddField(
            model_name='matrix',
            name='aggregator',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.PROTECT, related_name='aggregatorHW', to='base0.aggregator'),
        ),
    ]
