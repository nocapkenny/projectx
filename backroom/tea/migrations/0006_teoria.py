# Generated by Django 5.0.1 on 2024-03-30 15:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tea', '0005_alter_stud_group'),
    ]

    operations = [
        migrations.CreateModel(
            name='teoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, null=True)),
                ('text', models.CharField(max_length=5000, null=True)),
            ],
        ),
    ]
