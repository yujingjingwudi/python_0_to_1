

def login():
    return ("三玖天下第一")


def index():
    return ("雷姆举世无双")


def application(environ,start_response):
    start_response('200 OK',[('Content-Type','text/html;charset="utf-8"')])
    filepath = environ['file']
    if filepath == '/login.pyy':
        return login()
    elif filepath == '/index.pyy':
        return index()
    else:
        return "hello,world,三玖天下第一"