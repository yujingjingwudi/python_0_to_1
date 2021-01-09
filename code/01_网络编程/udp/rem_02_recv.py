import socket

def main():
    #创建套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定一个本地信息
    localaddr = ('',8083)
    s.bind(localaddr)
    while True:
        #接收数据,接收到的数据是一个元组，第一个元素是接收到的信息，第二个元素是发送方的地址
        recvdata = s.recvfrom(1024)
        meg = recvdata[0].decode("gbk")
        send_msg = recvdata[1]
        print("%s:%s" % (str(send_msg), meg))
    s.close()



if __name__ == "__main__":
    main()