# Generated by Django 5.1.4 on 2025-01-07 05:01

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0009_alter_teammembers_district_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammembers',
            name='biography',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
