from django.shortcuts import render
from django.http import HttpResponse
from .models import PicClass


# Create your views here.

FORBID_ADDR = ['192.168.1.4']

def forbid_user(func):
    def wrapper(request,*args,**kwargs):
        print("hello")
        userip = request.META['REMOTE_ADDR']
        if userip in FORBID_ADDR:
            return HttpResponse("FORBIDDEN")
        func(request,*args,**kwargs)
    return wrapper


def static_img(request):
    print(request.META['REMOTE_ADDR'])         # 192.168.1.4
    return render(request,'staticsmiddleware/static.html')

def exception(request):
    print(1/0)
    return HttpResponse('OK')

from django.conf import settings

def picture(request):
    return render(request,'staticsmiddleware/post-pic.html')

def postpic(request):
    # 1.获取上传的图片
    # 2.创建一个文件
    # 3.获取上传文件的内容并写到创建的文件中
    # 4.数据库中保存
    pic = request.FILES['pic']
    print(pic.name)
    pic_name = pic.name
    save_root = "%s/staticsmiddleware/%s"%(settings.MEDIA_ROOT,pic_name)
    with open(save_root,'wb') as f:
        for i in pic.chunks():
            f.write(i)

    PicClass.objects.create(picture='staticsmiddleware/%s'%(pic_name))
    return HttpResponse('ok')

from django.core.paginator import Paginator,Page

def showpic(request,mid):
    pics = PicClass.objects.all()
    paginator = Paginator(pics,1)
    print(paginator.num_pages)
    print("mid == " + str(mid))
    if mid=='':
        mid = 1
    page = paginator.page(mid)
    # print(page.picture)
    return render(request,'staticsmiddleware/showpic.html',{'page':page})