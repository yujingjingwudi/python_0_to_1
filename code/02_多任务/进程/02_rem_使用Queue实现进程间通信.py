import multiprocessing
import time


def download_file(temp):
    file = ("aa","bb","cc","dd","ee")
    for i in file:
        temp.put(i)
    print("文件传输完毕")

def deal_file(temp):
    new_file = list()
    while True:
        new_file.append(temp.get())
        if temp.empty():
            break
    print(new_file)
    print("消息处理完毕")


queue = multiprocessing.Queue()

def main():
    p1 = multiprocessing.Process(target=download_file,args = (queue,))
    p2 = multiprocessing.Process(target=deal_file,args = (queue,))
    p1.start()
    p2.start()

if __name__ == "__main__":
    main()