def dance():
    while True:
        print("跳舞")
        yield


def sing():
    while True:
        print("唱歌")
        yield


def main():
    t1 = dance()
    t2 = sing()
    while True:
        next(t1)
        next(t2)


if __name__ == "__main__":
    main()