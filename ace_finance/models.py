from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Create your models here.
class User_account(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="account")
    balance = models.IntegerField(default=0)
    accountNumber = models.IntegerField(default = None) #Generate an account number for the user
    
    def __str__(self):
        return f"Username:{self.user.username}, Balance: {self.balance}, Account Number: {self.accountNumber}"