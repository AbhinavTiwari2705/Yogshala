# Generated by Django 4.0.6 on 2023-04-14 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Main', '0006_yoga_how_to_yoga_type_yoga_level'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='yoga',
            name='How_to',
        ),
        migrations.AddField(
            model_name='yoga',
            name='Position',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
