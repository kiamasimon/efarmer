# Generated by Django 2.2.1 on 2019-05-31 08:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accountant', '0008_auto_20190531_0752'),
    ]

    operations = [
        migrations.RenameField(
            model_name='sale',
            old_name='customer_name',
            new_name='customer',
        ),
    ]
