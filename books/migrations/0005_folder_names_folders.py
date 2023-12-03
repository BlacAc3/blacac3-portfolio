# Generated by Django 4.2.4 on 2023-10-11 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0004_alter_book_shelf_pagesnumber'),
    ]

    operations = [
        migrations.CreateModel(
            name='Folder_Names',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder_name', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Folders',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('folder', models.ManyToManyField(to='books.folder_names')),
            ],
        ),
    ]