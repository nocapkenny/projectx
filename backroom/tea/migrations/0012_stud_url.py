# Generated by Django 5.0.1 on 2024-04-13 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0011_osenith'),
    ]

    operations = [
        migrations.AddField(
            model_name='stud',
            name='url',
            field=models.URLField(blank=True, max_length=150, unique=True),
        ),
    ]