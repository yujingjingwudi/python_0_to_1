import os,time
import multiprocessing


def copy_file(fileName,old_fileName,new_fileName,queue):
    f1 = open(old_fileName + '/' + fileName,'rb')
    content = f1.read()
    f1.close()

    f2 = open(new_fileName + '/' + fileName,'wb')
    f2.write(content)
    f2.close()
    queue.put(fileName)
    #print("文件%s复制完成" % (fileName))



def main():
    old_fileName = input("请输入需要拷贝的文件夹的名字")
    fileNames = os.listdir('./'+old_fileName)
    new_fileName = old_fileName + '[副本]'
    try:
        os.mkdir(new_fileName)
    except:
        pass
    file_nums = len(fileNames)

    pool = multiprocessing.Pool(5)
    queue = multiprocessing.Manager().Queue()
    copy_Ok =0

    # print(fileNames)

    for fileName in fileNames:
        # print(fileName)
        pool.apply_async(copy_file,(fileName,old_fileName,new_fileName,queue))

    pool.close()
    while True:
        file_name = queue.get()
        copy_Ok = copy_Ok + 1
        print("\r目前复制已完成%.2f %%" % (copy_Ok*100/file_nums),end='')
        if copy_Ok>=file_nums:
            break



if __name__ == "__main__":
    main()