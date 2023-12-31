# Generated by Django 4.2.4 on 2023-10-24 09:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('books', '0011_collection_name_user_notes_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='Book_reviews',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bookId', models.CharField(max_length=100)),
                ('title', models.CharField(max_length=200)),
                ('content', models.CharField(max_length=1000)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userReviews', to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
