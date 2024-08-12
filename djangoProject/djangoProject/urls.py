"""
URL configuration for djangoProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.urls import include  # برای اضافه کردن URL باید nclude رو فراخوانی کرد

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('home.urls')),

#  با این خط می تونم به URL های app home سترسی داشت
# اسم URL home میزارم و URL های App home و باهاش include می کنم
#  بجای home می تونم هیچی نزارم
]
