# Generated by Django 3.1.8 on 2021-04-13 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0005_remove_leftside_bstsmout'),
    ]

    operations = [
        migrations.AddField(
            model_name='leftside',
            name='BsTsmOut',
            field=models.OneToOneField(default='n/a', on_delete=django.db.models.deletion.PROTECT, to='base0.bsouttsm'),
        ),
    ]