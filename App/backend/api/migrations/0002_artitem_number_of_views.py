# Generated by Django 4.1.2 on 2022-12-18 11:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='artitem',
            name='number_of_views',
            field=models.IntegerField(default=0),
        ),
    ]
