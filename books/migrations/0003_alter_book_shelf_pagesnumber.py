# Generated by Django 4.2.4 on 2023-10-10 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0002_book_shelf_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_shelf',
            name='pagesNumber',
            field=models.IntegerField(blank=True),
        ),
    ]
