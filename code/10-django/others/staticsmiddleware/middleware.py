from django.http import HttpResponse


class middlewaretest:
    def __init__(self,get_response):
        self.get_response = get_response
        print("第一次调用")
    def __call__(self, request):
        response = self.get_response(request)
        return response
    def process_view(self,request,view_func,*args,**kwargs):
        print("调用processview")

    def process_request(self, request):
        print("这是一个中间件 --> test2")
        return HttpResponse("OK")
    def process_response(self,request,response):
        print("调用processresponse")
        return response
#
class middlewareexception:
    def __init__(self,get_response):
        self.get_response = get_response
        print("年号")
    def __call__(self, request):
        response = self.get_response(request)
        return response
    def process_exception(self,request,exception):
        print("peocessexception")