import multiprocessing
import time


def train1():
    while True:
        print('1')
        time.sleep(1)


def train2():
    while True:
        print('2')
        time.sleep(1)


if __name__ == "__main__":
    p1 = multiprocessing.Process(target=train1)
    p2 = multiprocessing.Process(target=train2)
    p1.start()
    p2.start()
    while True:
        print('3')
        time.sleep(1)