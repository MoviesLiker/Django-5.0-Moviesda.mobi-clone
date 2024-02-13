# Generated by Django 5.0.2 on 2024-02-13 11:37

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_name', models.CharField(max_length=255)),
                ('file_size', models.CharField(max_length=255)),
                ('vide_size', models.CharField(max_length=255)),
                ('format', models.CharField(max_length=255)),
                ('duration', models.CharField(max_length=255)),
                ('add_on', models.CharField(max_length=255)),
                ('server1', models.TextField()),
                ('server2', models.TextField()),
                ('movie', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.movie')),
            ],
        ),
    ]
