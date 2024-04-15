# Generated by Django 5.0.3 on 2024-03-24 20:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='email_add',
            field=models.EmailField(blank=True, max_length=254, verbose_name='email address'),
        ),
        migrations.AlterField(
            model_name='author',
            name='first_name',
            field=models.CharField(blank=True, max_length=15),
        ),
        migrations.AlterField(
            model_name='author',
            name='surname',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]