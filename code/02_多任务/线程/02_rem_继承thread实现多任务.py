import threading
import time


class Mythread(threading.Thread):
    def run(self):
        for i in range(5):
            time.sleep(1)
            print(i)
        print(self.name)
        self.fun1()
        self.fun2()

    def fun1(self):
        print("三玖")

    def fun2(self):
        print("雷姆")


if __name__ == "__main__":
    t1 = Mythread()
    t1.start()
    for i in range(6,10):
        time.sleep(1)
        print(i)