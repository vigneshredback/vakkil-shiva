# Generated by Django 5.1.4 on 2025-01-04 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammenbers',
            name='facebook',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammenbers',
            name='instagram',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammenbers',
            name='linkedin',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='teammenbers',
            name='twitter',
            field=models.URLField(blank=True, max_length=100, null=True),
        ),
    ]
