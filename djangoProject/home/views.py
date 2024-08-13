from django.http import HttpResponse  #  اگر خواسته باشم یک پاسخ ساده رو برگردونم این رو فرامی خونم
from django.shortcuts import render  #  گر خواسته باشم داده های پیچیده رو برگردومن از render استفاده میکنه
from .models import Todo  #  برای دسترسی به اطلاعات یک جدول از دیتابیس باید ایمپرت بشه
#  view یک تابع هست که یک درخواستی رو میگیره و پاسخی رو میده
#  همه ی توابه حتما باید یک چیزی رو return کنن
#  تابع view

def home(request):
   all = Todo.objects.all()  #  همه اطلاعات رو توی all میریزه
   return render(request, 'home.html', context = {'todo':all})  #  اطلاعات All رستاده میشه به فایل home.html
def say_hello(request): # مه ی تابع های view باید ارگومان اولشون request باشه
   person = {'name': 'amir hossein'}  #  برای کار کردن با اطلاعات باید اطلاعات تایپشون دیکشنری باشه
#   return HttpResponse('Hello World!')
   return render(request,'hello_html.html' , context = person) #  برای فرستادن اطلاعات به صفحه html اید اونا رو توی context

def ditals(request, todo_id):
   todo = Todo.objects.get(id=todo_id)  #  متد get یک رکورد خاص از جدول رو میکیره
   return render(request, 'ditals.html', {'todo':todo})