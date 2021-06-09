# Generated by Django 3.2.4 on 2021-06-08 09:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0006_auto_20210608_0932'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='identifier',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='movies',
            name='show_times',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='homepage.showtimes'),
        ),
        migrations.AlterField(
            model_name='showtimes',
            name='movie_identifer',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='theatres',
            name='showtimes',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='homepage.showtimes'),
        ),
        migrations.AlterField(
            model_name='time',
            name='time',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]