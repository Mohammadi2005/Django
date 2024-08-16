from django.shortcuts import redirect
from django.http import HttpResponse  #  اگر خواسته باشم یک پاسخ ساده رو برگردونم این رو فرامی خونم
from django.shortcuts import render  #  گر خواسته باشم داده های پیچیده رو برگردومن از render استفاده میکنه
from .models import Todo  #  برای دسترسی به اطلاعات یک جدول از دیتابیس باید ایمپرت بشه
from .FORMS import TodoCreateForm  #  فرمی که توی فایل FORM اختم رو فراخوانی میکنم
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

from django.contrib import messages  #  message رو برای استفاده import می کنم
def delete(request, todo_id):
   todo = Todo.objects.get(id=todo_id)
   todo.delete()
   messages.success(request, 'Todo deleted', extra_tags='success')  #  پیغام برای موفقیت امیز بودن
   return redirect('home')  #  redirect باعث مستقیما به یک ادرس دیگه بتونیم بریم

def back(request):
   return redirect('home')

def create(request):
   if request.method == 'POST':
      form = TodoCreateForm(request.POST)  #  اطلاعات وارد شده رو برای فرم میفرستم
      if form.is_valid():  # بررسی میکنه اطلاعات معتبر باشه
#  اگر اطلاعات معتبر باشه میریزدشون توی یک دیکشنری به نام کلین دیتا
          cd = form.cleaned_data
          Todo.objects.create(title=cd['title'], created=cd['created'], body=cd['body']) # سمت چپی ها اسامی فیلد های فایلا مدل هستند و سمت راستی ها اسامی فیلد های فرم هستند
          messages.success(request, 'Todo created successfully', extra_tags='success')
          return redirect('home')
   else:
      form = TodoCreateForm()  #  یک شی میسازم و برای فایل اچ تی ام ال میفرستم
   return render(request, 'create.html', {"form":form})

from .FORMS import TodoUpdateForm

def update(request, todo_id):
   todo = Todo.objects.get(id=todo_id)
   if request.method == 'POST':
      form = TodoUpdateForm(request.POST, instance=todo)
      if form.is_valid():
         form.save()
         messages.success(request, 'Todo updated successfully', extra_tags='success')
         return redirect('ditals', todo_id)
   else:
      form = TodoUpdateForm(instance=todo)  #  instans باعث میشه اطلاعاتtodo ریخته بشه توی فرم

   return render(request, "update.html", {"form":form})