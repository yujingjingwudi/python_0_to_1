import gevent
from gevent import monkey
import time

monkey.patch_all() # 这句话会将程序中所有的耗时操作替换成gevent目录下的方法

def fun1(num):
    for i in range(num):
        print(gevent.getcurrent(),i)   # gevent.getcurrent()，返回的是当前的spawn对象
        time.sleep(0.5)



def main():
    # g1 = gevent.spawn(fun1,5)
    # g2 = gevent.spawn(fun1,5)
    # g3 = gevent.spawn(fun1,5) # 返回的是一个grennlet对象
    # g1.join()
    # g2.join()
    # g3.join()
    gevent.joinall([gevent.spawn(fun1,5),
                    gevent.spawn(fun1,5),
                    gevent.spawn(fun1,5)])


if __name__ == "__main__":
    main()