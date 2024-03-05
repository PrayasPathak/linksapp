# Generated by Django 5.0.3 on 2024-03-05 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Link',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('url', models.URLField(max_length=120)),
                ('slug', models.SlugField(blank=True, unique=True)),
                ('clicks', models.PositiveIntegerField(default=0)),
            ],
        ),
    ]