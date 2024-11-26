# Generated by Django 4.2.16 on 2024-11-26 02:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Actor',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('photo_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Director',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('name', models.CharField(max_length=255)),
                ('photo_url', models.URLField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Genre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tmdb_id', models.IntegerField(blank=True, null=True, unique=True)),
                ('title', models.CharField(max_length=255)),
                ('release_date', models.DateField(blank=True, null=True)),
                ('poster_image_url', models.URLField(blank=True, null=True)),
                ('plot', models.TextField(blank=True, default='')),
                ('rating', models.FloatField(default=0)),
                ('adult', models.BooleanField(default=False)),
                ('budget', models.IntegerField(default=0)),
                ('revenue', models.IntegerField(default=0)),
                ('popularity', models.FloatField(default=0)),
                ('runtime', models.IntegerField(default=0)),
                ('tagline', models.TextField(blank=True, default='')),
                ('vote_count', models.IntegerField(default=0)),
                ('trailer_url', models.URLField(blank=True, null=True)),
                ('is_now_playing', models.BooleanField(default=False)),
                ('is_popular', models.BooleanField(default=False)),
                ('actors', models.ManyToManyField(related_name='movies', to='movies.actor')),
                ('director', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='movies', to='movies.director')),
                ('genres', models.ManyToManyField(related_name='movies', to='movies.genre')),
                ('likes', models.ManyToManyField(blank=True, related_name='liked_movies', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
