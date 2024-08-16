from django import forms  #  باید اول فرم رو ایمپورت کنم
from .models import Todo

#  یک کلاس باید برای فرم بسازم

class TodoCreateForm(forms.Form):  #  باید از فرم ارث بری کنیم دقی قا شبیه مدل
    title = forms.CharField(required=False)  #  اگر required برابر با false باشه این داده غیر ضروری میشه
    body = forms.CharField(label="BODY")  #
    created = forms.DateTimeField()

class TodoUpdateForm(forms.ModelForm):  #  ModelForm باعث میشه که صورت اتومات بشه فرم رو ساخت
    class Meta:
        model = Todo
        fields = ['title', 'body', 'created']
     #  fields = '__all__'


