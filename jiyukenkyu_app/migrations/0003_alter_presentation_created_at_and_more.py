# Generated by Django 4.1.2 on 2022-10-18 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('jiyukenkyu_app', '0002_alter_presentation_created_at_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='presentation',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='presentation',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
