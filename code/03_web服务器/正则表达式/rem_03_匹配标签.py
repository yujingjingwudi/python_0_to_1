import re


def main():
    ret = re.match("<(?P<title1>\w*)><(?P<title2>\w*)>\w*</(?P=title2)></(?P=title1)>","<body><h1>niao</h1></body>")
    if ret:
        print(ret.group(1))

if __name__ == "__main__":
    main()