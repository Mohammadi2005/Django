
from django.contrib import admin
from django.urls import path
from django.urls import include  # برای اضافه کردن URL باید nclude رو فراخوانی کرد

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),
    path('account/', include('account.urls')),

#  با این خط می تونم به URL های app home سترسی داشت
# اسم URL home میزارم و URL های App home و باهاش include می کنم
#  بجای home می تونم هیچی نزارم
]
