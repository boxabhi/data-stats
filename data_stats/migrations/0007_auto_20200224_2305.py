# Generated by Django 2.2.6 on 2020-02-24 17:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data_stats', '0006_business_political_technology'),
    ]

    operations = [
        migrations.AlterField(
            model_name='business',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='political',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='technology',
            name='id',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]