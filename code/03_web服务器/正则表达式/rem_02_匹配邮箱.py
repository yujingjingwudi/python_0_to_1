import re

def main():
    mail = input("请输入邮箱")
    ret = re.match(r"[a-zA-Z0-9]{4,20}@(qq|gmail|163|136).com",mail)
    if ret:
        print("{0}符合要求".format(mail))
    else:
        print("{0}不符合要求".format(mail))


if __name__ == "__main__":
    main()