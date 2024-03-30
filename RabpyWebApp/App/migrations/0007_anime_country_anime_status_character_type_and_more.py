# Generated by Django 5.0.3 on 2024-03-30 10:50

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0006_remove_anime_genre_anime_genre'),
    ]

    operations = [
        migrations.AddField(
            model_name='anime',
            name='country',
            field=models.CharField(default='Japanese', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='anime',
            name='status',
            field=models.CharField(default='Finished', max_length=50),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='character',
            name='type',
            field=models.CharField(default='Main', max_length=10),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='ResourceAnime',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('anime', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.anime')),
            ],
        ),
        migrations.CreateModel(
            name='ResourceCharacter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('url', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('character', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='App.character')),
            ],
        ),
    ]