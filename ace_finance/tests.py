from django.test import TestCase
from django.contrib.auth.models import User
from django.utils import timezone
from .models import User_account, Beneficiaries, Notification, Transaction_user
from .views import accountNumberGenerator, send_money, create_transaction_id

class UserModelTest(TestCase):
    def setUp(self):
        # Create a test user
        self.user = User.objects.create(username="testuser", password="testpassword")
        self.user_account = User_account.objects.create(user=self.user)

    def test_user_account_creation(self):
        
        self.assertEqual(self.user_account.balance, 1000)
        self.assertEqual(self.user_account.accountNumber, 0)

    def test_beneficiaries_creation(self):
        beneficiary_account = User_account.objects.create(user=User.objects.create(username="beneficiary", password="beneficiary"))
        beneficiaries = Beneficiaries.objects.create(user_account=self.user_account, beneficiary_user=beneficiary_account)
        self.assertEqual(beneficiaries.date_time.date(), timezone.now().date())

    def test_transaction_user_creation(self):
        sender_account =self.user_account
        recipient_account = User_account.objects.create(user=User.objects.create(username="recipient", password="recipient"))
        transaction = Transaction_user.objects.create(sender=sender_account, recipient=recipient_account, amount=500, note="Test transaction", transaction_id="123")
        self.assertEqual(transaction.date_time.date(), timezone.now().date())

    def test_notification_creation(self):
        # Create a test notification
        notification = Notification.objects.create(
            noti_user_account=self.user_account,
            notification_status="not_read",
            notification_title="Test Notification",
            notification_details="Test Details"
        )

        # Check if the notification was created successfully
        self.assertEqual(Notification.objects.count(), 1)

        # Retrieve the created notification from the database
        created_notification = Notification.objects.first()

        # Check if the fields have the correct values
        self.assertEqual(created_notification.noti_user_account, self.user_account)
        self.assertEqual(created_notification.notification_status, "not_read")
        self.assertEqual(created_notification.notification_title, "Test Notification")
        self.assertEqual(created_notification.notification_details, "Test Details")

    def test_notification_status_choices(self):
        # Attempt to create a notification with an invalid status
        with self.assertRaises(ValueError):
            Notification.objects.create(
                noti_user_account=self.user_account,
                notification_status="invalid_status",
                notification_title="Invalid Status Notification",
                notification_details="Test Details"
            )