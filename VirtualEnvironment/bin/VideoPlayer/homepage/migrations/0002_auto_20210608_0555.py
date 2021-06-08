# Generated by Django 3.2.4 on 2021-06-08 05:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homepage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.CharField(max_length=100, primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=50)),
                ('rating', models.CharField(max_length=10)),
                ('poster', models.CharField(max_length=200)),
            ],
        ),
        migrations.DeleteModel(
            name='Video',
        ),
    ]
