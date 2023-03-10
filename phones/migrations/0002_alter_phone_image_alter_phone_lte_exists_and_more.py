# Generated by Django 4.1.7 on 2023-03-02 13:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('phones', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='phone',
            name='image',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='phone',
            name='lte_exists',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='phone',
            name='price',
            field=models.CharField(max_length=50),
        ),
        migrations.AlterField(
            model_name='phone',
            name='release_date',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='phone',
            name='slug',
            field=models.SlugField(max_length=400),
        ),
    ]
