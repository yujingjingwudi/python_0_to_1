# encoding: utf-8
# URL_DIR = {
#     "/login.pyy":login,
#     "/index.pyy":index
# }
import re


#给路由添加正则的原因：在实际开发中，往往往往会带着很多参数，例如 /add/000006.html,000006就是参数
#原有正则的话，会需要写n次@trans_url，字典中也会存储n个键值对，使用正则的话能够让一个函数同时能够处理多个页面

URL_DIR = dict()

def trans_url(url):
    def set_func(fuction):
        URL_DIR[url] = fuction
        def call_function(*args,**kwargs):
            return fuction()
        return call_function
    return set_func

@trans_url(r"/login.html")
def login(ret):
    with open("./template/login.html","rb") as f:
        return  f.read()
    # return ("三玖天下第一")

@trans_url(r"/index.html")
def index(ret):
    with open("./template/index.html","rb") as f:
        return f.read()

@trans_url(r"/ham.html")
def index(ret):
    with open("./template/ham.html","rb") as f:
        return f.read()

@trans_url(r"/add/(\d+)\.html")
def number_url(ret):
    return "OK------%s"%ret.grout(1)




def application(environ,start_response):
    # 状态码和一个字典，存放着响应头的数据
    start_response('200 OK',[('Content-Type','text/html;charset="utf-8"')])

    filepath = environ['file']
    print(URL_DIR)
    try:
        """
            # URL_DIR = {
#               "/login.html":login,
#               "/index.html":index
#               "/
        }    
        """
        for key,value in URL_DIR.items():
            ret = re.match(key,filepath)
            if ret:
                return value(ret)
            else:
                print("正则没有返回值")
        else:
            return "没有对应的函数"
        # ret = URL_DIR[filepath]
        # return ret()
    except Exception as ex:
        return ("没找到该页面%s" % ex)
    # if filepath == '/login.pyy':
    #     return login()
    # elif filepath == '/index.pyy':
    #     return index()
    # else:
    #     return "hello,world,三玖天下第一"