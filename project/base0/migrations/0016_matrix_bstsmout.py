# Generated by Django 3.1.8 on 2021-04-13 12:26

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0015_matrix'),
    ]

    operations = [
        migrations.AddField(
            model_name='matrix',
            name='BsTsmOut',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.PROTECT, to='base0.bsouttsm'),
        ),
    ]
