# Generated by Django 4.0.4 on 2022-05-17 21:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0004_follow_created_at_alter_follow_from_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='artitem',
            name='artitem_image',
            field=models.ImageField(default='artitem/defaultart.jpg', upload_to='artitem/'),
        ),
        migrations.AlterField(
            model_name='artitem',
            name='tags',
            field=models.ManyToManyField(blank=True, to='api.tag'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='from_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.myuser'),
        ),
        migrations.AlterField(
            model_name='follow',
            name='to_user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='api.myuser'),
        ),
        migrations.AlterField(
            model_name='myuser',
            name='followers',
            field=models.ManyToManyField(related_name='follower', through='api.Follow', to='api.myuser'),
        ),
    ]
