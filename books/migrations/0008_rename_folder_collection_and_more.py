# Generated by Django 4.2.4 on 2023-10-13 11:54

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0007_folder_books'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Folder',
            new_name='Collection',
        ),
        migrations.RenameModel(
            old_name='Folder_Name',
            new_name='Collection_name',
        ),
    ]