


def fibonacci(num):
    a = 0
    b = 1
    count = 0
    while count<num:
        p = yield a
        print("ret = {0}".format(p))
        a = b
        b = a + b
        count += 1


def main():
    a = fibonacci(10)
    # 第一个不能send内容
    ret = a.send("年后")
    print(ret)
    print(next(a))
    print(next(a))

if __name__ == "__main__":
    main()