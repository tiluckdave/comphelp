# Generated by Django 3.1.5 on 2021-01-23 17:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('datastructures', '0007_dspostcomment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='date',
            field=models.DateField(default=django.utils.timezone.now),
        ),
    ]
