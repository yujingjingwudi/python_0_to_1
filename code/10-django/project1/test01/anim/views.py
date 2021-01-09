from django.shortcuts import render

# Create your views here.

from .models import ProductionInfo,WifeInfo
def show_productions(request):
    productions = ProductionInfo.objects.all()
    wife = WifeInfo.objects.all()
    print("*********************************************")
    print(len(productions))
    print(len(wife))
    wifes = WifeInfo.objects.all()
    return render(request, 'anim/index.html',{'productions':productions})

def show_actor(request,bid):
    # 根据bid查询作品信息
    pro = ProductionInfo.objects.get(id=bid)
    wifes = pro.wifeinfo_set.all()

    return render(request, 'anim/act.html',{'wifes':wifes,'production':pro})
