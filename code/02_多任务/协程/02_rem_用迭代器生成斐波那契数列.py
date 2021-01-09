class Fabonacci:
    def __init__(self,num):
        self.num = num
        self.a = 0
        self.b = 1
        self.count = 0
        self.date =0

    def __iter__(self):
        return self

    def __next__(self):
        if self.count<self.num:
            self.date = self.a
            self.a,self.b = self.b,self.a+self.b
            self.count = self.count + 1
            return self.date
        else:
            raise StopIteration



def main():
    fabonacci = Fabonacci(10)
    for i in fabonacci:
        print(i)



if __name__ == "__main__":
    main()