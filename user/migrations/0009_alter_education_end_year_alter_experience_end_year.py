# Generated by Django 5.1 on 2024-08-19 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0008_education_experience_testimony'),
    ]

    operations = [
        migrations.AlterField(
            model_name='education',
            name='end_year',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='experience',
            name='end_year',
            field=models.DateField(null=True),
        ),
    ]
