from greenlet import greenlet
import time


def progress1():
    while True:
        time.sleep(0.5)
        print("三玖")
        p2.switch()

def progress2():
    while True:
        time.sleep(0.5)
        print("雷姆")
        p1.switch()

p1 = greenlet(progress1)
p2 = greenlet(progress2)
p1.switch()