# Generated by Django 4.0.5 on 2022-07-06 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0012_alter_profile_bank'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bank',
            field=models.CharField(default='-', max_length=255),
        ),
    ]
