from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import User_account, Beneficiaries, Transaction_user
from .views import accountNumberGenerator, send_money, create_transaction_id

class UserModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username="testuser", password="testpassword")

    def test_user_account_creation(self):
        user_account = User_account.objects.create(user=self.user)
        self.assertEqual(user_account.balance, 1000)
        self.assertEqual(user_account.accountNumber, 0)

    def test_beneficiaries_creation(self):
        user_account = User_account.objects.create(user=self.user)
        beneficiary_account = User_account.objects.create(user=User.objects.create(username="beneficiary", password="beneficiary"))
        beneficiaries = Beneficiaries.objects.create(user_account=user_account, beneficiary_user=beneficiary_account)
        self.assertEqual(beneficiaries.date_time.date(), timezone.now().date())

    def test_transaction_user_creation(self):
        sender_account = User_account.objects.create(user=self.user)
        recipient_account = User_account.objects.create(user=User.objects.create(username="recipient", password="recipient"))
        transaction = Transaction_user.objects.create(sender=sender_account, recipient=recipient_account, amount=500, note="Test transaction", transaction_id="123")
        self.assertEqual(transaction.date_time.date(), timezone.now().date())

