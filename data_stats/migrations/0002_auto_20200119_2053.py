# Generated by Django 3.0.2 on 2020-01-19 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_stats', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=1000),
        ),
    ]
