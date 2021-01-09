import socket


def main():
    # 创建套接字
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    # 绑定地址，IP一般为空
    locelAddr = ("",7890)
    service_socket.bind(locelAddr)
    # 套接字变为接收模式
    service_socket.listen(128)
    # 等待客户的连接，并为客户分配新的套接字
    while True:
        print("正在等待用户连接")
        client_socket,client_addr = service_socket.accept()
        print("正在为%s服务" % str(client_addr))
        while True:
            recvdata = client_socket.recv(1280)
            if recvdata:
                print("收到请求"+recvdata.decode("gbk"))
                client_socket.send("你好".encode("gbk"))
            else:
                client_socket.close()
                print("服务结束，有请下一位")
                break
    service_socket.close()



if __name__ == "__main__":
    main()