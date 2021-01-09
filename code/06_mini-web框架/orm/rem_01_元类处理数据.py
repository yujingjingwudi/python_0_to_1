import logging



class MedelMetaclasee(type):
    def __new__(cls,name,base,attrs):
        mappings = dict()
        for k,v in attrs.items():
            if isinstance(v,tuple):
                mappings[k] = v

        for k in mappings.keys():
            attrs.pop(k)

        attrs['__mappings__'] = mappings
        attrs['__table__'] = name                         # __table__ 是表名
        return type.__new__(cls,name,base,attrs)


class User(metaclass = MedelMetaclasee):
    uid = ('uid', 'int unsigned')
    name = ('name', 'varchar(30)')
    email = ('email', 'varchar(300)')
    password = ('password', 'varchar(30)')
    """
    __mappings__ = {
    'uid':('uid','int unsigned'),
    'name':('name','varchar(30)'),
    'email':('email','varchar(300),
    'password':('password','varchar(30)
    }
    """
    def __init__(self,**kwargs):
        for key,value in kwargs.items():
            setattr(self,key,value)

    def sava(self):
        fields = []
        args = []
        for k,v in self.__mappings__.items():
            fields.append(v[0])
            args.append(getattr(self,k,None))

        args_list = list()
        for i in args:
            if isinstance(i,int):
                args_list.append(str(i))
            elif isinstance(i,str):
                args_list.append("""'%s'""" % i)

        sql = "insert into %s (%s) values (%s)" % (self.__table__,','.join(fields),','.join(args_list))
        print(sql)

u = User(uid = 12345, name="Michael", email = 'test@orm.org', password = 'mw-pwd')
u.sava()