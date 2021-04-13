# Generated by Django 3.1.8 on 2021-04-13 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0016_matrix_bstsmout'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='matrix',
            name='id',
        ),
        migrations.AddField(
            model_name='matrix',
            name='BsTsmIn',
            field=models.OneToOneField(default='', on_delete=django.db.models.deletion.PROTECT, primary_key=True, serialize=False, to='base0.bsintsm'),
        ),
    ]