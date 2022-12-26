# Generated by Django 4.1.2 on 2022-12-23 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('history', '0003_history_exhibition_id_history_is_exhibition'),
    ]

    operations = [
        migrations.RenameField(
            model_name='history',
            old_name='is_exhibition',
            new_name='is_exhibition_off',
        ),
        migrations.AddField(
            model_name='history',
            name='is_exhibition_on',
            field=models.BooleanField(default=False),
        ),
    ]