import time


def login():
    return "welcome my website -----%s------" % time.ctime()

def sayhello():
    return "say hello -----%s------" % time.ctime()

def call():
    return "三九天下第一啊啊啊啊啊 -----%s------" % time.ctime()




def applictaion(fileName):
    if fileName == '/login.py':
        return login()
    elif fileName == '/sayhello.py':
        return sayhello()
    elif fileName == '/call.py':
        return call()
    else:
        return '404'