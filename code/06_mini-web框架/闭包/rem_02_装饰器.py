
#-*- coding: UTF-8 -*-


def func1(func):
    def func2():
        print("123")
        print("3454")
        return func()
    return func2

@func1    # 等价于test1 = func1(test1)
def test1():
    print("nihoa")

# ret = func1(test1)
# ret()	
test1()