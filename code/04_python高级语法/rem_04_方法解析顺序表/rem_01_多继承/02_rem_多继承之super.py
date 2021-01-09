

class Parent(object):
    def __init__(self,name,*args,**kwargs):
        print("Parent的构造方法被调用")
        self.name = name


    def xxx(self):
        pass

    def xxxx(self):
        pass

class SonA(Parent):
    def __init__(self,name,gender,*args,**kwargs):
        print("SonA的构造方法被调用")
        # Parent.__init__(self,"son1")
        super().__init__(name,*args,**kwargs)
        self.gender = gender


class SonB(Parent):
    def __init__(self,name,wife,*args,**kwargs):
        print("SonB的构造方法被调用")

        super().__init__(name,*args,**kwargs)
        # Parent.__init__(self,name)
        self.wife = wife

class grandSon(SonA,SonB):
    def __init__(self,name,gender,wife):
        print("孙子的构造方法被调用")
        super().__init__(name,gender,wife)
        # super().__init__(name,wife)

        #SonA.__init__(self,name,gender)
        #SonB.__init__(self,name,wife)

print(grandSon.__mro__)
yangcheng = grandSon("yangcheng","girl","dake")







