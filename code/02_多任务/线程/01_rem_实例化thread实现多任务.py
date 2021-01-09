import threading
import time


def sing():
    for i in range(5):
        print("*******sing" + str(i) + "********")
        time.sleep(1)


def dance():
    for i in range(5):
        print("*******dance" + str(i) + "********")
        time.sleep(1)


if __name__ == "__main__":
    t1 = threading.Thread(target=sing)
    t2 = threading.Thread(target=dance)
    print(threading.enumerate())
    t1.start()
    t2.start()
    while True:
        print(threading.enumerate())
        if len(threading.enumerate())<=2:
            break
        time.sleep(1)
