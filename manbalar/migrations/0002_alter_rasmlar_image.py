# Generated by Django 5.0.1 on 2024-01-12 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manbalar', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rasmlar',
            name='image',
            field=models.ImageField(upload_to='images/'),
        ),
    ]
