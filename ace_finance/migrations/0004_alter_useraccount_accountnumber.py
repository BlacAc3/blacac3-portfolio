# Generated by Django 4.2.4 on 2024-01-07 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ace_finance', '0003_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='useraccount',
            name='accountNumber',
            field=models.IntegerField(default=None),
        ),
    ]
