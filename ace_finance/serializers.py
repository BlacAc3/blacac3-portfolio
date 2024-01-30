from rest_framework import serializers
from .models import Transaction_user

class TransactionUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Transaction_user
        fields = "__all__"