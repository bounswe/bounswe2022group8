# Generated by Django 4.1.2 on 2022-12-17 14:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='artitem',
            name='type',
        ),
        migrations.AddField(
            model_name='artitem',
            name='category',
            field=models.CharField(choices=[('AR', 'Architecture'), ('SC', 'Sculpture'), ('DR', 'Drawing'), ('PH', 'Photography'), ('PR', 'Prints'), ('PA', 'Painting/Acrylic'), ('PO', 'Painting Oilpaint'), ('PW', 'Painting Watercolour'), ('PD', 'Painting Digital'), ('PM', 'Painting Mural'), ('PG', 'Painting Gouache'), ('PP', 'Painting Pastel'), ('PE', 'Painting Encaustic'), ('PF', 'Painting Fresco'), ('PS', 'Painting Spray'), ('OP', 'Painting Other'), ('OT', 'Other')], default='OT', max_length=2),
        ),
    ]
