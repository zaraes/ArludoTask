# Generated by Django 3.2.4 on 2021-06-08 14:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0008_alter_showtimes_times'),
    ]

    operations = [
        migrations.RenameField(
            model_name='time',
            old_name='time',
            new_name='time1',
        ),
        migrations.AddField(
            model_name='time',
            name='time2',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='time3',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='time4',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='time5',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='time',
            name='time6',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
