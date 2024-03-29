# Generated by Django 4.2.4 on 2024-01-09 13:31

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='User_account',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance', models.IntegerField(default=0)),
                ('accountNumber', models.IntegerField(default=0)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='account', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Transactions',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('note', models.CharField(max_length=200)),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('recipient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_transactions_recipient', to='ace_finance.user_account')),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='my_transactions_sender', to='ace_finance.user_account')),
            ],
        ),
        migrations.CreateModel(
            name='Beneficiaries',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('beneficiary_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='a_recipient_to', to='ace_finance.user_account')),
                ('user_account', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='beneficiaries', to='ace_finance.user_account')),
            ],
        ),
    ]
