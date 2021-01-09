import threading
import time


def niao1():
    global sum
    for i in range(1000000):
        mudex.acquire()
        sum = sum + 1
        mudex.release()
    print("test1中num==%d" % (sum))


def niao2():
    global sum
    for i in range(1000000):
        mudex.acquire()
        sum = sum + 1
        mudex.release()
    print("test1中num==%d" % (sum))


sum = 0
mudex = threading.Lock()


def main():
    t1 = threading.Thread(target=niao1)
    t2 = threading.Thread(target=niao2)
    t1.start()
    t2.start()
    time.sleep(2)
    print("主线程中sum==%d" % (sum))

if __name__ == "__main__":
    main()