# Generated by Django 3.0.2 on 2020-01-19 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('data_stats', '0002_auto_20200119_2053'),
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('content_id', models.IntegerField(primary_key=True, serialize=False)),
                ('content', models.CharField(max_length=5000)),
                ('created_at', models.DateField(auto_now=True)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='data_stats.Category')),
            ],
        ),
    ]