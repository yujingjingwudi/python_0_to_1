# encoding: utf-8
def login():
    with open("./template/login.html","rb") as f:
        return  f.read()
    # return ("三玖天下第一")


def index():
    with open("./template/index.html","rb") as f:
        return f.read()


def application(environ,start_response):
    # 状态码和一个字典，存放着响应头的数据
    start_response('200 OK',[('Content-Type','text/html;charset="utf-8"')])
    filepath = environ['file']
    if filepath == '/login.pyy':
        return login()
    elif filepath == '/index.pyy':
        return index()
    else:
        return "hello,world,三玖天下第一"