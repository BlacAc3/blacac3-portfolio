from rest_framework import serializers
from .models import *


class UserAccountSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = User_account
        fields = "__all__"


class TransactionUserSerializer(serializers.ModelSerializer):
    sender = UserAccountSerializer()
    recipient = UserAccountSerializer()

    class Meta:
        model = Transaction_user
        fields = ["sender", "recipient", "amount"]
