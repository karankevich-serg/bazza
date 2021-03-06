# Generated by Django 3.1.8 on 2021-04-15 09:00

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    dependencies = [
        ('base0', '0020_auto_20210415_0855'),
    ]

    operations = [
        migrations.CreateModel(
            name='Object',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('slug', django_extensions.db.fields.AutoSlugField(blank=True, editable=False, populate_from='title')),
                ('last_updated', models.DateTimeField(auto_now=True)),
                ('city', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('vertical', models.CharField(max_length=255)),
                ('plinth', models.CharField(max_length=255)),
                ('pair', models.CharField(max_length=255)),
                ('ts0', models.CharField(choices=[('1', 'ts1'), ('2', 'ts2'), ('3', 'ts3'), ('4', 'ts4'), ('5', 'ts5'), ('6', 'ts6'), ('7', 'ts7'), ('8', 'ts8'), ('9', 'ts9'), ('10', 'ts10'), ('11', 'ts11'), ('12', 'ts12'), ('13', 'ts13'), ('14', 'ts14'), ('15', 'ts15'), ('16', 'ts16'), ('17', 'ts17'), ('18', 'ts18'), ('19', 'ts19'), ('20', 'ts20'), ('21', 'ts21'), ('22', 'ts22'), ('23', 'ts23'), ('24', 'ts24'), ('25', 'ts25'), ('26', 'ts26'), ('27', 'ts27'), ('28', 'ts28'), ('29', 'ts29'), ('30', 'ts30'), ('31', 'ts31')], default='', max_length=2)),
                ('tsm', models.CharField(choices=[('1', 'tsm1'), ('2', 'tsm2')], default='', max_length=2)),
                ('streamDirection', models.OneToOneField(on_delete=django.db.models.deletion.PROTECT, related_name='stream_direction', to='base0.direction')),
                ('tsToBs', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='base0.bsintsm')),
                ('ts_1', models.ForeignKey(default='', null=True, on_delete=django.db.models.deletion.PROTECT, related_name='TS1', to='base0.timeslot')),
            ],
        ),
        migrations.DeleteModel(
            name='Stream',
        ),
    ]
