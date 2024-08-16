#  وقتی کاربر URL hello رو وارد کنه تابع say_hello اجرا میشه
#  باید به URL صلی پروزه دسترسی به URL app رو بدیم
from django.urls import path
from . import views

urlpatterns = [
    path('hello/', views.say_hello, name='hello'),  #  وقتی hello رو جست و جو کنم say_hello اجرا میشه
    path('', views.home, name='home'),
    path('ditals/<int:todo_id>', views.ditals, name='ditals'),#  قتی یک ditals همراه یک عدد بیاد میره سراغ تابع ditals
#   'ditals/<int:todo_id>' اسم ادرس
#  رو ditals میزاره و با اسم ادرس کار میکنه
    path('delete/<int:todo_id>', views.delete, name='delete'),
    path('back', views.back, name='back'),
    path('create', views.create, name='create'),
    path('update/<int:todo_id>', views.update, name='update'),
]
