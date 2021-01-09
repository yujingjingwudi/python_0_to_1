from django.shortcuts import render
from .models import BookInfo,RoleInfo
# Create your views here.


def tem_val(request):
    my_book = BookInfo.objects.get(id=1)
    my_list = [1,2,3,4]
    my_dict = {'rem':100}
    context = {'my_book':my_book,'my_list':my_list,'my_dict':my_dict}
    return render(request,'template_filters/temp_val.html',context)

def tem_tag(request):
    books = BookInfo.objects.all()
    return render(request,'template_filters/temp_tag.html',{'books':books})

def inhertOfPa(request):
    return render(request,'template_filters/base.html')

def inhertOfChild(request):
    return render(request,'template_filters/child.html')

def escape(request):
    return render(request,'template_filters/temp_excape.html',{'content':'<h1>这是一个标签</h1>'})