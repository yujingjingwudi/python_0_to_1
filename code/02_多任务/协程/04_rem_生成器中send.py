def febonacii(num):
    a = 0
    b = 1
    count = 0
    while count < num:
        ret = yield a
        print(ret)
        a,b = b,a+b
        count = count + 1
    return "abc"


def main():
    f1 = febonacii(10)
    # yield a 的值传到 next(f1)，a的值赋给ret
    ret = next(f1)
    print(ret)
    # "哈哈哈哈哈"传给第六行的ret，再次运行到yield a中，将a传到a
    ret = f1.send("哈哈哈哈哈哈")
    print(ret)

    '''while True:
        try:
            print(next(f1))
        except Exception as ret:
            #ret捕获到了生成器中的返回值
            print(ret.value)
            break'''


if __name__ == "__main__":
    main()
