# Generated by Django 3.2.4 on 2021-06-04 14:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0002_post'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='title',
        ),
    ]