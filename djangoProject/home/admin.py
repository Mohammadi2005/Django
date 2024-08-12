from django.contrib import admin
from .models import Todo
#  برای اضافه کردن مدل ها به admin panl باید اونا رو impport کنم

# Register your models here.

admin.site.register(Todo)