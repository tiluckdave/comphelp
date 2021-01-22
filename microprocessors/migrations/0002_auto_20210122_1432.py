# Generated by Django 3.1.5 on 2021-01-22 09:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('microprocessors', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='content',
            new_name='code',
        ),
        migrations.AddField(
            model_name='post',
            name='explain',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image1',
            field=models.ImageField(default='', upload_to='images/data-structures'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='image2',
            field=models.ImageField(default='', upload_to='images/data-structures'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='intro',
            field=models.TextField(default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='mainImage',
            field=models.ImageField(default='', upload_to='images/data-structures'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='post',
            name='slug',
            field=models.CharField(default='', max_length=130),
            preserve_default=False,
        ),
    ]
