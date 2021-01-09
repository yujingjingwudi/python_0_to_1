



class yuanlei(type):
    def __new__(clas,class_name,parent_name,yuansu):

        for key,value in yuansu.items():
            if not key.startswith("__"):
                yuansu[key.upper()] = yuansu.pop(key)

        return type(class_name,parent_name,yuansu)




class test_clase(object,metaclass=yuanlei):
    bar = "bin"

A = test_clase()
print(A.BAR+"你好")