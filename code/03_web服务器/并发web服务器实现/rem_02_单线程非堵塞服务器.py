import socket
import time


def main():
    service_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    service_socket.bind(("",7890))
    service_socket.listen(128)
    # 将套接字设置为非堵塞状态
    service_socket.setblocking(False)
    socket_list = list()
    while True:
        time.sleep(0.5)
        try:
            new_socket,local_addr = service_socket.accept()
            print("有用户连接成功")
        except:
            print("没有用户连接")
        else:
            new_socket.setblocking(False)
            socket_list.append(new_socket)

        for sock in socket_list:
            try:
                recvdata = sock.recv(1280)
            except:
                print("该用户没有发送信息")
            else:
                if recvdata:
                    print(recvdata.decode("utf-8"))
                else:
                    sock.close()
                    socket_list.remove(sock)





if __name__ == "__main__":
    main()