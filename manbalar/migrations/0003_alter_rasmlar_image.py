# Generated by Django 5.0.1 on 2024-01-12 10:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manbalar', '0002_alter_rasmlar_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasmlar',
            name='image',
            field=models.ImageField(upload_to=''),
        ),
    ]
