# Generated by Django 4.2.4 on 2024-01-21 17:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0015_remove_publicshelf_shelf_alter_publicshelf_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book_reviews',
            name='bookId',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book_reviews',
            name='content',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book_reviews',
            name='title',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='book_shelf',
            name='description',
            field=models.TextField(blank=True),
        ),
        migrations.AlterField(
            model_name='notes',
            name='content',
            field=models.TextField(),
        ),
    ]