# Generated by Django 5.0.1 on 2024-04-01 18:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0006_teoria'),
    ]

    operations = [
        migrations.AddField(
            model_name='teoria',
            name='docfile',
            field=models.FileField(null=True, upload_to=''),
        ),
        migrations.AlterField(
            model_name='teoria',
            name='name',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='teoria',
            name='text',
            field=models.CharField(max_length=5000),
        ),
    ]
