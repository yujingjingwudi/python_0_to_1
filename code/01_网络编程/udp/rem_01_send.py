import socket

#发送方
def main():
    #创建套接字
    s = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #发送方没有绑定端口的时候，os会随机分配一个端口
    #输入数据
    meg=''
    while meg!="quit":
        meg = input("请输入信息")
        s.sendto(meg.encode("utf-8"), ("192.168.1.10",8081))
    s.close()



if __name__ == "__main__":
    main()