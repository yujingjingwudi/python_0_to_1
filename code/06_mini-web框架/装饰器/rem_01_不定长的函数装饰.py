




def set_fun1(func):
    def create_func(*args,**kwargs):
        print("haha")
        print("hahaha")
        func(*args,**kwargs)
    return  create_func     

@set_fun1
def function(a,*args,**kwargs):
    print("多参数函数装饰%d"%a)
    print("多参数函数装饰",args)
    print("多参数函数装饰",kwargs)


function(100)
function(100,200)
function(100,200,300,name=300)