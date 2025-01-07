# Generated by Django 5.1.4 on 2025-01-06 06:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_teammenbers_district'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teammenbers',
            name='consultant',
            field=models.CharField(choices=[('draft', 'Draft'), ('published', 'Published'), ('archived', 'Archived')], default='unknown', max_length=100),
        ),
        migrations.AlterField(
            model_name='teammenbers',
            name='district',
            field=models.CharField(choices=[('chennai', 'chennai'), ('vellore', 'vellore'), ('coimbatore', 'coimbatore')], default='chennai', max_length=100),
        ),
        migrations.DeleteModel(
            name='Consultants',
        ),
        migrations.DeleteModel(
            name='Districts',
        ),
    ]
