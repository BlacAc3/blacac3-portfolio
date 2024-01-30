from django.urls import path
from . import views

urlpatterns = [
    path("", views.indexView),
    path("get-result/", views.runPythonCode),

]