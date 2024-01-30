from rest_framework import serializers
from .models import *

class TransactionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_user
        fields = "__all__"

class UserAccountSerializer(serializers.ModelSerializer):
    transactions= TransactionUserSerializer(many=True)
    class Meta:
        model = User_account
        fields = ["id","balance", "transactions"]


