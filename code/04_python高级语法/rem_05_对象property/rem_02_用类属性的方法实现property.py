



class A():
    def __init__(self):
        self.__a = 0
    def get_a(self):
        return self.__a
    def set_a(self,value):
        self.__a = value
    a = property(get_a,set_a)


b = A()
print(b.a)
b.a = 300
print(b.a)