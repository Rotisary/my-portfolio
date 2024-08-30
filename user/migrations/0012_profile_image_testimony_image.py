# Generated by Django 5.1 on 2024-08-27 01:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0011_remove_testimony_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='image',
            field=models.ImageField(null=True, upload_to='profile_pic'),
        ),
        migrations.AddField(
            model_name='testimony',
            name='image',
            field=models.ImageField(null=True, upload_to='writer_pics'),
        ),
    ]
