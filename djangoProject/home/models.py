from django.db import models

# Create your models here.
class Todo(models.Model):
#  باید فیلد های جداول دیتابیس به عنوان پراپری قرار بگیرن
    title = models.CharField(max_length=100)
    body = models.TextField()  #  رای اطلاعات خیلی زیاد استفاده میشه
    created = models.DateTimeField()
#  بعد از ساخت مدل باید اعمالشون کنیم روی دیتابیس
#  برای اعمال روی دیتابیس دو تا مرحله داریم

# 1
#  باید به جنگو بگم این کد رو طوری تغییر بده که sqlite بفهمتش
#  توی ترمینال باید دستور زیر بزنم
#  pyrhon manage.py makemigration
#  این دستور می گرده توی مدل و تغییراتی که ایجاد شده باشه رو اعمال می کنه
#  فایل initial توی migration ه شکلی ایجاد میشه sqlite بفهمتش

# 2
#  حالا باید migration رو روی دیتابیس sqlite اعمال کنم
#  دستور زیر رو توی دیتابیس باید بزنم
#  python manage.py migrate
#  ین دستور migration ها رو روی دیتابیس اعمال میکنه و به تعداد migration به ما ok میده


#  برای اضافه کردن مدل ها به admin panl باید وارد فایل admin app بشم
