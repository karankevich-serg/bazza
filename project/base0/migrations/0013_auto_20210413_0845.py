# Generated by Django 3.1.8 on 2021-04-13 08:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0012_leftside_bstsmout'),
    ]

    operations = [
        migrations.AddField(
            model_name='bsintsm',
            name='tsm',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterUniqueTogether(
            name='bsintsm',
            unique_together={('tsm', 'bs')},
        ),
    ]
