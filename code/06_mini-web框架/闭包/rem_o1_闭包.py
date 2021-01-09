




def line(k,b):
    def create_line(x):
        print(k*x+b)
    return create_line


niaonimamabie = line(3,4)
niaonimamabie(3)