# Generated by Django 2.2.1 on 2019-05-31 09:29

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('auth', '0011_update_proxy_permissions'),
        ('admin', '0003_logentry_add_action_flag_choices'),
        ('accountant', '0009_auto_20190531_0845'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Admin',
            new_name='Admin_User',
        ),
    ]