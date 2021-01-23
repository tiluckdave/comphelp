# Generated by Django 3.1.5 on 2021-01-22 14:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('computergraphics', '0002_auto_20210122_1309'),
    ]

    operations = [
        migrations.CreateModel(
            name='Links',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('short', models.TextField(max_length=200)),
                ('link', models.CharField(max_length=1000)),
            ],
        ),
        migrations.CreateModel(
            name='Mcqs',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('question', models.CharField(max_length=1000)),
                ('option1', models.CharField(max_length=100)),
                ('option2', models.CharField(max_length=100)),
                ('option3', models.CharField(max_length=100)),
                ('option4', models.CharField(max_length=100)),
                ('date', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('sno', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=200)),
                ('short', models.TextField(max_length=300)),
                ('file', models.FileField(upload_to='notes/data-structures')),
                ('date', models.DateField()),
            ],
        ),
    ]