# Generated by Django 4.0.5 on 2022-07-09 19:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('split_app', '0010_alter_obligation_payment_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='obligation',
            name='payment_date',
            field=models.DateField(blank=True, default='2022-01-01', null=True),
        ),
    ]
