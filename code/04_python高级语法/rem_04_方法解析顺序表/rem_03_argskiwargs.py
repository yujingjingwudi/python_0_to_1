

def aaa(a,b,*args,**kwargs):
    print(a)
    print(b)
    # print(*args)
    print(args)
    print(kwargs)
    # print(**kwargs)


def bbb(a,b,*args,**kwargs):
    print(a)
    print(b)
    print(args)
    print(kwargs)
    # aaa(a,b,args,kwargs)              # 11 22 ((33,44),{'age':18,'name':'yangcheng'}
    # aaa(a,b,*args,kwargs)             # 11 22 (33, 44, {'age': 18, 'name': 'yangcheng'}) {}
    # aaa(a,b,args,**kwargs)              # 11 22 ((33, 44),){'age': 18, 'name': 'yangcheng'}
    aaa(a,b,*args,**kwargs)
bbb(11,22,33,44,name="yangcheng",age=18 )