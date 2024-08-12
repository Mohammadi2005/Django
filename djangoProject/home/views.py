
from django.http import HttpResponse  #  اگر خواسته باشم یک پاسخ ساده رو برگردونم این رو فرامی خونم
from django.shortcuts import render  #  گر خواسته باشم داده های پیچیده رو برگردومن از render استفاده میکنه
# Create your views here.

#  view یک تابع هست که یک درخواستی رو میگیره و پاسخی رو میده
#  همه ی توابه حتما باید یک چیزی رو return کنن
#  تابع view

def home(request):
   return render(request, 'home.html')
def say_hello(request): # مه ی تابع های view باید ارگومان اولشون request باشه

#   return HttpResponse('Hello World!')
   return render(request,'hello_html.html')