# Generated by Django 2.2.1 on 2019-05-31 07:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0005_auto_20190526_1836'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='number_of_units',
            field=models.IntegerField(default=12),
            preserve_default=False,
        ),
    ]