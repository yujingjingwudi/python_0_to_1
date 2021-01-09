from django.shortcuts import render
from .models import BookInfo,RoleInfo
from datetime import datetime
from django.http import HttpResponse,HttpResponseRedirect,JsonResponse
# Create your views here.


def indexpage(request):
    books = BookInfo.objects.all()
    return render(request,'bookpage/book_page.html',{'books':books})

def additem(request):
    book = BookInfo()
    book.btitle = "末日时在做什么，能不能再见一面"
    book.bpub_date = datetime(2010,2,5)
    book.save()
    return HttpResponseRedirect('book')

def deleteitem(request,bid):
    book = BookInfo.objects.get(id=bid)
    book.delete()
    return HttpResponseRedirect('book')
#   效果等同于 redirect('book')

def select(request):
    return render(request,'bookpage/select.html')

def getpro(request):
    books = BookInfo.objects.all()
    book_list = []
    for book in books:
        book_list.append((book.id,book.btitle))
    return JsonResponse({'data': book_list})

def getroles(request,mid):
    book = BookInfo.objects.get(id=mid)
    roles = book.roleinfo_set.all()
    # roles = RoleInfo.objects.filter(Rbook__id=mid)
    role_list = []
    for role in roles:
        role_list.append((role.id, role.Rname))
    return JsonResponse({'data': role_list})