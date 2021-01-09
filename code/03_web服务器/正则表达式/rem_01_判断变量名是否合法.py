import re


def main():
    names = ["__main__", "2la_niu", "_name", "name"]
    for name in names:
        ret = re.match(r"[a-zA-Z_]+\w*",name)
        if ret:
            print(ret.group())
        else:
            print("%s不合法" % name)


if __name__ == "__main__":
    main()