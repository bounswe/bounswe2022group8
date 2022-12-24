# Generated by Django 4.1.2 on 2022-12-21 13:24

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_rename_salestatus_artitem_sale_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='artitem',
            name='bought_by',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='bought_art', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='bid',
            name='accepted',
            field=models.CharField(choices=[('RE', 'Rejected'), ('AC', 'Accepted'), ('NR', 'No Response')], default='NR', max_length=2),
        ),
    ]