from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def setSession(request):
    request.session['name'] = 'rem'
    request.session['age'] = 16
    return render(request,'redis-test/redis-session-get.html')

def getSession(request):
    name = request.session['name']
    age = request.session['age']
    return HttpResponse(name + "+" + str(age))