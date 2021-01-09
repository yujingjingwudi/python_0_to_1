def febonacii(num):
    a = 0
    b = 1
    count = 0
    while count < num:
        yield a
        a,b = b,a+b
        count = count + 1


def main():
    f1 = febonacii(10)
    #print(f1)
    print(next(f1))
    print(next(f1))
    #for i in f1:
    #    print(i)


if __name__ == "__main__":
    main()
