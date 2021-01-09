from django.shortcuts import render,redirect
from django.http import JsonResponse,HttpResponse


# Create your views here.
def login(request):
    if request.session.has_key('isLogin'):
        return render(request,'login/index.html')
    else:
        if 'username' in request.COOKIES:
            userName = request.COOKIES['username']
        else:
            userName = ''
        return render(request,'login/login.html',{'username':userName})

def login_chect(request):

    userName = request.POST.get('user')
    passWord = request.POST.get('pwd')
    rem = request.POST.get('rem')
    print(rem)
    print(userName + passWord)
    if userName == 'yujingjing' and passWord == '19970806':
        request.session['isLogin'] = 'yes'
        return JsonResponse({'res':1})
    else:
        if rem == 'on':
            print("保存cookie")
            response = JsonResponse({'res':0})
            response.set_cookie('username',userName,max_age=7*24*3600)
            return response
        else:
            return JsonResponse({'res':0})

def index(request):
    return render(request,'login/index.html')