# Generated by Django 4.2.13 on 2024-05-19 10:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='CategoryID',
            new_name='category_id',
        ),
        migrations.RenameField(
            model_name='category',
            old_name='CategoryName',
            new_name='category_name',
        ),
    ]
