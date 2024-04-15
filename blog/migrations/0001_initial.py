# Generated by Django 5.0.3 on 2024-03-24 19:51

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Author',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=15, null=True)),
                ('surname', models.CharField(max_length=30, null=True)),
                ('email_add', models.EmailField(max_length=254, null=True, verbose_name='email address')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tags', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('excerpt', models.CharField(max_length=200)),
                ('image_name', models.CharField(max_length=100)),
                ('date', models.DateField(auto_now=True)),
                ('slug', models.SlugField(default='', unique=True)),
                ('content', models.TextField()),
                ('author', models.ForeignKey(default='Anonymous', on_delete=django.db.models.deletion.SET_DEFAULT, related_name='posts', to='blog.author')),
                ('tags', models.ManyToManyField(to='blog.tag')),
            ],
        ),
    ]