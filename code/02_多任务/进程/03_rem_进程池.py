import multiprocessing
import random,os,time


def worker(num):
    t_start = time.time()
    print("开始执行任务%s,进程号是%s" % (num,os.getpid()))
    time.sleep(random.random()*2)
    t_end = time.time()
    print("任务%s执行完毕，执行耗时%0.2f" % (num,t_end-t_start))


def main():
    pool = multiprocessing.Pool(3)
    for i in range(10):
        pool.apply_async(worker,(i,))
    pool.close()
    pool.join()


if __name__ == "__main__":
    main()