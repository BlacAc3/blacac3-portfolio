from django.urls import path
from . import views

urlpatterns=[

    # rendering pages 
    path("", views.index, name="finance_index"),
    path("activities/", views.financial_activities, name="financial_activities"),
    path("beneficiaries/", views.beneficiaries, name="beneficiaries"),
    path("my-profile/", views.profile, name="finance_profile"),
    path("login/", views.login_register, name="finance_login"),
    path("notifications/", views.notification, name="notification"),

    # 
    path("send/", views.send_money, name="send_money"),

    # Javascript functions
    path("account-number/", views.check_account_number),
]