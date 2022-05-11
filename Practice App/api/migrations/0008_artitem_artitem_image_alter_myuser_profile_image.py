# Generated by Django 4.0.4 on 2022-05-11 12:22

import api.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0007_myuser_profile_image_alter_tag_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='artitem',
            name='artitem_image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.get_artitem_path),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='profile_image',
            field=models.ImageField(blank=True, null=True, upload_to=api.models.get_avatar_path),
        ),
    ]
