import threading
import time


def load_mesg(temp):
    time.sleep(1)
    temp.append(33)
    print("test1的temp为"+str(temp))

def ad_mesg(temp):
    print("test2的temp为"+str(temp))


lalala = [11,22]


if __name__ == "__main__":
    # target表示新建线程的位置，args传递参数，注：必须要以元组的形式传递参数
    t1 = threading.Thread(target=load_mesg,args=(lalala,))
    t2 = threading.Thread(target=ad_mesg,args=(lalala,))

    t1.start()

    t2.start()
    print("主线程lalala = %s" % (str(lalala)))