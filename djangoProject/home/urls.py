#  وقتی کاربر URL hello رو وارد کنه تابع say_hello اجرا میشه
#  باید به URL صلی پروزه دسترسی به URL app رو بدیم
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello),
]
