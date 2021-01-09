import socket


def main():
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    local_Addr = ("",7890)
    service_socket.bind(local_Addr)
    service_socket.listen(128)
    while True:
        print("等待连接")
        new_socket,client_addr = service_socket.accept()
        print("成功连接用户" + str(client_addr))
        filename = new_socket.recv(1280).decode("gbk")
        print("用户所需要的文件是" + filename)
        file_Content=''
        try:
            f = open(filename,"rb")
            file_Content = f.read()
        except Exception as ex:
            print("不存在该文件")
        if file_Content:
            new_socket.send(file_Content)
        new_socket.close()




if __name__ == "__main__":
    main()