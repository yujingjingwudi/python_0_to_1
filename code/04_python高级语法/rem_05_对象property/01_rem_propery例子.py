



class page(object):
    def __init__(self,page):
        self.page = page
        self.item = 20

    @property
    def start(self):
         return (self.page-1)*self.item

    @start.setter
    def start(self,value):
        self.start = value

    @start.deleter
    def start(self):
        del self.start


    @property
    def end(self):
        return self.page*self.item

# a = page(1 )
# print(a.start)
# print(a.end)
a = page(1)
print(a.start)
a.start = 10