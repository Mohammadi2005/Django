
from django.http import HttpResponse  #  اگر خواسته باشم یک پاسخ ساده رو برگردونم این رو فرامی خونم
from django.shortcuts import render
# Create your views here.

#  view یک تابع هست که یک درخواستی رو میگیره و پاسخی رو میده
#  همه ی توابه حتما باید یک چیزی رو return کنن
#  تابع view

def say_hello(request): # مه ی تابع های view باید ارگومان اولشون request باشه
#   return render(request, 'hello_html.html')
   return HttpResponse('Hello World!')