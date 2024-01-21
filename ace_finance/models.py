from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class User_account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account")
    balance = models.BigIntegerField(default=1000)
    accountNumber = models.BigIntegerField(default=0) #Generate an account number for the user
    
    def __str__(self):
        return f"Username:{self.user.username}, Balance: {self.balance}, Account Number: {self.accountNumber}"
    
class Beneficiaries(models.Model):
    user_account = models.ForeignKey(User_account, on_delete=models.CASCADE, related_name="beneficiaries")
    beneficiary_user=models.ForeignKey(User_account, on_delete=models.CASCADE, related_name="a_recipient_to")
    date_time = models.DateTimeField(default=timezone.now)


class Transaction_user(models.Model):
    sender = models.ForeignKey(User_account, on_delete=models.CASCADE, related_name="sender_transactions")
    recipient=models.ForeignKey(User_account, on_delete=models.CASCADE, related_name="receiver_transactions")
    amount=models.BigIntegerField(default=0)
    note = models.CharField(max_length=200)
    date_time = models.DateTimeField(default=timezone.now)
    transaction_id=models.CharField(max_length=100)

