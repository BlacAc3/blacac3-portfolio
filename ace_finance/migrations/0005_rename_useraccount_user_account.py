# Generated by Django 4.2.4 on 2024-01-07 20:49

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('ace_finance', '0004_alter_useraccount_accountnumber'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='UserAccount',
            new_name='User_account',
        ),
    ]
