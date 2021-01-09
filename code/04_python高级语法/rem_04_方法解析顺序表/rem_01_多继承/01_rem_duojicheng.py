
class Parent(object):
    def __init__(self ,name):
        print("Parent的构造方法被调用")
        self.name = name


    def xxx(self):
        pass

    def xxxx(self):
        pass

class SonA(Parent):
    def __init__(self ,name ,gender):
        print("SonA的构造方法被调用")
        Parent.__init__(self ,"son1")
        self.gender = gender


class SonB(Parent):
    def __init__(self ,name ,wife):
        print("SonB的构造方法被调用")
        Parent.__init__(self ,name)
        self.wife = wife

class grandSon(SonA ,SonB):
    def __init__(self ,name ,gender ,wife):
        print("孙子的构造方法被调用")
        SonA.__init__(self ,name ,gender)
        SonB.__init__(self ,name ,wife)

yangcheng = grandSon("yangcheng" ,"girl" ,"dake")













