# Generated by Django 5.0.3 on 2024-04-06 09:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_comment'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='user_name',
            field=models.CharField(blank=True, default='Anonymous', max_length=50),
        ),
    ]
