# Generated by Django 3.1.5 on 2021-01-21 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=255)),
                ('subject', models.CharField(choices=[('ds', 'Data Structures'), ('cg', 'Compuetr Graphics'), ('dt', 'Digital Techniques'), ('mp', 'Microprocessors'), ('new', 'New Subject (put your subject in below text feild)')], max_length=255)),
                ('content', models.TextField()),
            ],
        ),
    ]
