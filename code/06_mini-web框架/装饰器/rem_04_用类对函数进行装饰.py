



class A():
    def __init__(self,func):
        self.func = func

    def __call__(self):
        print("__call__方法")
        return self.func()

    @staticmethod
    def printthing(function):
        def set_thing():
            function()
        return  set_thing



@A.printthing
def function():
    return "这个是一个方法"

print(function())