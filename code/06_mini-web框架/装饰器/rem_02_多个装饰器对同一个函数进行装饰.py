








def add_privilige(function):
    print("装饰器add正在装载")
    def set_add(*args,**kwargs):
        print("装饰器add正在执行")
        function(*args,**kwargs)
    return set_add

def add_xxxvilige(function):
    print("装饰器xxx正在装载")
    def set_xxx(*args,**kwargs):
        print("装饰器xxx正在执行")
        function(*args,**kwargs)
    return set_xxx


# 一个函数同时被两个装饰器装饰时候，先装载下面的后装载上面的，先执行上面的，在装载下面的
@add_privilige
@add_xxxvilige
def function():
    print("nihaoya")

function()