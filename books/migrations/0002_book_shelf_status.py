# Generated by Django 4.2.4 on 2023-10-10 11:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book_shelf',
            name='status',
            field=models.CharField(choices=[('not_started', 'Not Started'), ('reading', 'Currently Reading'), ('finished', 'Finished Reading')], default='not_started', max_length=50),
        ),
    ]
