# Generated by Django 3.1.3 on 2022-12-19 10:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('onlinecourse', '0002_auto_20221219_1055'),
    ]

    operations = [
        migrations.AlterField(
            model_name='choice',
            name='is_correct',
            field=models.BooleanField(default=False),
        ),
    ]