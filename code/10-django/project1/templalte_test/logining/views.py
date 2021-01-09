from django.shortcuts import render,redirect
from django.http import response,HttpResponse
from django.urls import reverse
# Create your views here.


def login_required(func_login):
    def draw(require,*args,**kwargs):
        if require.session.has_key('islogin'):
            return func_login(require,*args,**kwargs)
        else:
            return redirect('/login/login')
    return draw

@login_required
def index(request):
    return render(request, 'login/index.html')


def login(request):
    if request.session.has_key('islogin'):
         return redirect('/login/index')
    else:
        if 'username' in request.COOKIES:
            username = request.COOKIES['username']
        else:
            username = ''
    return render(request,'login/loginpage.html',{'username':username})

def login_check(request):
    username = request.POST.get('user')
    password = request.POST.get('pwd')
    remember = request.POST.get('rem')

    print(username + password)
    if username == "yujingjing" and password == "19970806":
        response = redirect('/login/index')
        if remember == "on":
            response.set_cookie('username', username, max_age=7 * 24 * 3600)
        request.session['islogin'] = True
        return response
    else:
        response = redirect('/login/login')
        return response

def index2(request):
    return render(request,'login/index2.html')

def url_reverse(request):
    return render(request,'login/url_reverse.html')

def show_args(request,a,b):
    return HttpResponse(a+':'+b)

def show_kwargs(request,c,d):
    return HttpResponse(c+ ':' + d)



def test_redirect(request):
    url = reverse('logining:show_kwargs',kwargs={'c':3,'d':4})
    return redirect(url)